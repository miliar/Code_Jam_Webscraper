#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream input("B-large.in");
	ofstream out("a.out");
	int T;
	input>>T;
	int a[100][100];
	for(int i=0;i<T;i++)
	{
		int N,M; 
		input>>N>>M;
		for(int i1=0;i1<N;i1++)
			for(int j1=0;j1<M;j1++)
				input>>a[i1][j1];

		for(int k=0;k<100;k++)
		{
		//先找最小的
			int min =101;
			for(int i1=0;i1<N;i1++)
				for(int j1=0;j1<M;j1++)
				{
					if(a[i1][j1]<min&&a[i1][j1]!=-1)
						min=a[i1][j1];
				}
		//行
		for(int i1=0;i1<N;i1++)
		{
			int j1=0;
			for(;j1<M;j1++)
			{
				if(a[i1][j1]!=min&&a[i1][j1]!=-1)
					break;
			}
			if(j1==M)//这一行走完了,全标记为-1
			{
				for(int j2=0;j2<M;j2++)
					a[i1][j2]=-1;
			}
		}
		//列
		for(int j1=0;j1<M;j1++)
		{
			int i1=0;
			for(;i1<N;i1++)
			{
				if(a[i1][j1]!=min&&a[i1][j1]!=-1)
					break;
			}
			if(i1==N)//这一行走完了,全标记为-1
			{
				for(int i2=0;i2<N;i2++)
					a[i2][j1]=-1;
			}

		}
		}
		bool can=true;
		for(int i=0;i<N;i++)
			for(int j=0;j<M;j++)
				if(a[i][j]!=-1)
				{
					can=false;
					break;
				}
		
			if(can)
				out<<"Case #"<<i+1<<": YES"<<endl;
			else
				out<<"Case #"<<i+1<<": NO"<<endl;
	}


	input.close();
	out.close();
	return 0;
}
