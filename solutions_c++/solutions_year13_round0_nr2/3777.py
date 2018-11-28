#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string.h>
#include<cmath>
using namespace std;
#define N 120
int MAT[N][N];
int flag[N][N];
void input(int n,int m)
{
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			scanf("%d",&MAT[i][j]);
			flag[i][j]=0;
		}
}
void Cmput(int n,int m)
{
	int mam;
	for(int i=0;i<n;i++)
	{
		mam=MAT[i][0];
		for(int j=0;j<m;j++)
			if(mam<=MAT[i][j])
			{
				mam=MAT[i][j];
				flag[i][j]++;
			}
			mam=MAT[i][m-1];
		for(int j=m-1;j>=0;j--)
			if(mam<=MAT[i][j])
			{
				mam=MAT[i][j];
				flag[i][j]++;
			}
		for(int j=0;j<m;j++)
			if(flag[i][j]==1)flag[i][j]=0;
	}
	for(int j=0;j<m;j++)
	{
		mam=MAT[0][j];
		for(int i=0;i<n;i++)
			if(mam<=MAT[i][j])
			{
			mam=MAT[i][j];
			flag[i][j]++;
			}
		mam=MAT[n-1][j];
		for(int i=n-1;i>=0;i--)
			if(mam<=MAT[i][j])
			{
				mam=MAT[i][j];
				flag[i][j]++;
			}
		for(int i=0;i<n;i++)
			if(flag[i][j]==1)flag[i][j]=0;
	}	
}
int Judge(int n,int m)
{
	Cmput(n,m);
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	if(flag[i][j]==0 || MAT[i][j]>100)return 0;
	return 1;
}
int main(void)
{
	int T,cse=0,n,m;
	freopen("dataL.in","r",stdin);
	freopen("data.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&m);
		input(n,m);
		printf("Case #%d: ",++cse);
		if(Judge(n,m))		printf("YES\n");
		else				printf("NO\n");
	}

	return 0;
}
/*

*/