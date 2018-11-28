// code jam.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int map[101][101];
int t;
int m,n;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int T = 1;T<= t;T++)
	{
		cin>>m>>n;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
			{
				cin>>map[i][j];
			}
		bool flag = true;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
			{
				bool okx = true;
				bool oky = true;
				
				for(int k=0;k<m;k++)
					if(k!=i && map[k][j]>map[i][j])
						okx=false;
				for(int k=0;k<n;k++)
					if(k!=j && map[i][k]>map[i][j])
						oky=false;
				if(!okx && !oky)
				{
					flag=false;
					break;
				}
			}
		if(flag)
			cout<<"Case #"<<T<<": YES\n";
		else 
			cout<<"Case #"<<T<<": NO\n";
	}
	return 0;
}

