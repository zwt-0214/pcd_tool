#!/usr/bin/env python3
"""
STL到PCD转换脚本
将STL文件转换为高质量点云PCD文件
"""

import open3d as o3d
import os
import sys

def stl_to_pcd(stl_path, pcd_path, num_points=10000):
    """
    将STL文件转换为PCD点云文件
    
    参数:
    stl_path: 输入STL文件路径
    pcd_path: 输出PCD文件路径
    num_points: 生成点云的点数（默认10000）
    """
    # 检查输入文件是否存在
    if not os.path.exists(stl_path):
        print(f"错误: STL文件不存在 - {stl_path}")
        return False
    
    try:
        # 读取STL文件
        print(f"正在读取STL文件: {stl_path}")
        mesh = o3d.io.read_triangle_mesh(stl_path)
        
        if mesh.is_empty():
            print("错误: STL文件为空或无法读取")
            return False
        
        print(f"网格信息: {len(mesh.vertices)} 顶点, {len(mesh.triangles)} 三角面")
        
        # 生成均匀分布的点云
        print(f"正在生成包含 {num_points} 个点的点云...")
        pcd = mesh.sample_points_uniformly(number_of_points=num_points)
        
        # 可选：计算点云法向量（增加点云质量）
        pcd.estimate_normals()
        
        # 保存为PCD文件
        print(f"正在保存PCD文件: {pcd_path}")
        o3d.io.write_point_cloud(pcd_path, pcd, write_ascii=False)
        
        print(f"转换完成! 生成的PCD文件包含 {len(pcd.points)} 个点")
        return True
        
    except Exception as e:
        print(f"转换过程中出现错误: {str(e)}")
        return False

def main():
    # 定义输入输出路径
    
    input_path = "/home/zwt/E.STL"
    output_path = "/home/zwt/E_1w.pcd"
    
    # 执行转换
    success = stl_to_pcd(input_path, output_path, num_points=10000)
    
    if success:
        print(f"成功将 {input_path} 转换为 {output_path}")
        return 0
    else:
        print("转换失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())