#include<math.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<time.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

//typedef long long lld;
//typedef __int64 lld;//这里的时候要用long long
const int INF=1000000000;
const int MAX=110;
int mat[MAX][MAX];
//横
bool okh(int x,int y,int n,int m)
{
	int i,j;
	for(j=y+1;j<m;j++)
	{
		if(mat[x][j]>mat[x][y])return false;
	}
	for(j=y-1;j>=0;j--)
	{
		if(mat[x][j]>mat[x][y])return false;
	}
	return true;
}
//纵
bool okv(int x,int y,int n,int m)
{
	int i,j;
	for(i=x+1;i<n;i++)
	{
		if(mat[i][y]>mat[x][y])return false;
	}
	
	for(i=x-1;i>=0;i--)
	{
		if(mat[i][y]>mat[x][y])return false;
	}
	return true;
}
int main()
{
	int n,m;
	int i,j;
	int ans=INF;
	int T,CS=1;
	//freopen("E:\\ACM\\B-large.in","r",stdin);
	//freopen("E:\\ACM\\B-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&mat[i][j]);
			}
		}
		bool flag=true;
		for(i=0;i<n&&flag;i++)
		{
			for(j=0;j<m&&flag;j++)
			{
				if(!okh(i,j,n,m)&&!okv(i,j,n,m))
				{
					flag=false;
				}
			}
		}
		if(flag)printf("Case #%d: YES\n",CS++);
		else printf("Case #%d: NO\n",CS++);
	}
	return 0;
}
/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1


*/
