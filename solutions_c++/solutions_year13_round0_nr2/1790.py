#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
using namespace std;
#define N 110
int a[N][N],h[N][N],test,n,m,flag;

int main()
{
	scanf("%d",&test);
	for (int t=0;t<test;t++)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
			{
				scanf("%d",h[i]+j);
				a[i][j]=100;
			}
		for (int i=0;i<n;i++)
		{
			int temp=-0x7fffffff;
			for (int j=0;j<m;j++) 
				temp=max(temp,h[i][j]);
			for (int j=0;j<m;j++)
				a[i][j]=min(a[i][j],temp);
		}
		for (int j=0;j<m;j++)
		{
			int temp=-0x7fffffff;
			for (int i=0;i<n;i++)
				temp=max(temp,h[i][j]);
			for (int i=0;i<n;i++)
				a[i][j]=min(a[i][j],temp);
		}
		flag=1;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (a[i][j]!=h[i][j]) flag=0;
		printf("Case #%d: ",t+1);
		puts(flag?"YES":"NO");
	}
	return 0;
}