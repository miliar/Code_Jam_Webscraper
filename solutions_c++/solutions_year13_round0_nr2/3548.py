// googleCode.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<stdio.h>
int matrix[100][100];
using namespace std;
void init() {
	for(int i=0;i<100;i++) {
		for(int j=0;j<100;j++) {
			matrix[i][j] = 101;
		}
	}
};
bool hasWay(int x, int y, int n, int m) {
	bool flag = true;
	for (int i=0; i<m;i++) {
		if (matrix[x][y] < matrix[x][i]) {
			flag = false;
			break;
		}
	}
	if (flag) return true;
	flag = true;
	for (int i=0; i<n; i++) {
		if (matrix[x][y] < matrix[i][y]) {
			flag = false;
			break;
		}
	}
	return flag;
};
int main()
{
	freopen("data.in","r",stdin); //输入重定向，输入数据将从in.txt文件中读取   
	freopen("data.out","w",stdout); //输出重定向，输出数据将保存在out.txt文件中   
	
	int t;
	cin>>t;
	for (int x=1; x<=t; x++) {
		init();
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n; i++) {
			for(int j=0; j<m;j++) {
				cin>>matrix[i][j];
			}
		}
		bool flag = true;
		for(int i=0;i<n; i++) {
			for(int j=0; j<m;j++) {
				if (!hasWay(i,j,n,m) ){
					flag = false;
					break;
				}
			}
		}
		if (flag) cout<<"Case #"<<x<<": YES"<<endl;
		else cout<<"Case #"<<x<<": NO"<<endl;
	}
//	fclose(stdin);//关闭文件   
//	fclose(stdout);//关闭文件  
	return 0;
}