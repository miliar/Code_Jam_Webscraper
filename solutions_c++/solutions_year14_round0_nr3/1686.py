#include<iostream>
#include<stdio.h>
using namespace std;
int n,m,a[100][100],b[100][100],k;
int c[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
bool dp;
bool check(int x,int y)
{
	int i;
	for(i=0;i<8;i++)
		if (x+c[i][0]>=1&&x+c[i][0]<=n&&y+c[i][1]>=1&&y+c[i][1]<=m)
			if (a[x+c[i][0]][y+c[i][1]]==1)  return true;
	return false;
}
bool findzero()
{
	int i,j;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if (b[i][j]==0)  return false;
	return true;
}
void pig(int x,int y)
{
	int i;
	b[x][y]=1;
	if (check(x,y)) return ;
	for(i=0;i<8;i++)
		if (x+c[i][0]>=1&&x+c[i][0]<=n&&y+c[i][1]>=1&&y+c[i][1]<=m)
			if (a[x+c[i][0]][y+c[i][1]]==0&&b[x+c[i][0]][y+c[i][1]]==0) pig(x+c[i][0],y+c[i][1]);	
}
void dog()
{
	int i,j,k1,k2;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if (a[i][j]==0)
			{
				for(k1=1;k1<=n;k1++)
		          for(k2=1;k2<=m;k2++)
			          b[k1][k2]=a[k1][k2];
				b[i][j]=1;
				pig(i,j);
				if (findzero())
				{
					dp=true;
					a[i][j]=2;
					return ;
				}
			}
}
void dfs(int x,int y,int z)
{
	if (z==k)
	{
		dog();
		return ;
	}
	if (x>n) return ;
	if (m-y+1+(n-x)*m+z<k) return ;
	
	a[x][y]=1;
	if (y==m) dfs(x+1,1,z+1);
	else
		dfs(x,y+1,z+1);
    if (dp==true) return ;
	
	a[x][y]=0;
	if (y==m) dfs(x+1,1,z);
	else
		dfs(x,y+1,z);
	if (dp==true)  return ;
}
int main()
{
	int i,j,ii,tt;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("000.txt","w",stdout);
	scanf("%d",&tt);
	for(ii=1;ii<=tt;ii++)
	{
		scanf("%d%d%d",&n,&m,&k);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				a[i][j]=0;
		dp=false;
		dfs(1,1,0);
		if (dp==true)
		{
			printf("Case #%d:\n",ii);
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=m;j++)
				{
					if (a[i][j]==0) printf(".");
					if (a[i][j]==1) printf("*");
					if (a[i][j]==2) printf("c");
				}
				printf("\n");
			}
		}
		else
		{
			printf("Case #%d:\n",ii);
			printf("Impossible\n");
		}
	}

	
}