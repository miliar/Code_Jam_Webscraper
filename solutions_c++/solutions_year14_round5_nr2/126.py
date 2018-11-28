/*
Author: elfness@UESTC
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long LL;
const int V=110;
int dp[V][V*10][V*10];
int h[V],g[V],P,Q,n;
int a[V][150],b[V][150],c[V][150],t[V];
int _;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d%d%d",&P,&Q,&n);
		for(int i=0;i<n;i++)
		scanf("%d%d",&h[i],&g[i]);
		for(int i=0;i<n;i++)
		{
			t[i]=0;
			for(int j=0;j<=10;j++)
			for(int k=0;k<=10;k++)
			{
				if(k!=0&&Q*k+j*P>=h[i]&&Q*(k-1)+j*P<h[i])
				{
					c[i][t[i]]=0;
					a[i][t[i]]=j;
					b[i][t[i]++]=k;
				}
				if(j!=0&&Q*k+(j-1)*P<h[i]&&Q*k+j*P>=h[i])
				{
					c[i][t[i]]=1;
					a[i][t[i]]=j;
					b[i][t[i]++]=k;
				}
			}
		}
		for(int i=0;i<=n;i++)
		for(int j=0;j<=i*10;j++)
		for(int k=0;k<=i*10;k++)
		dp[i][j][k]=-1;
		dp[0][0][0]=0;
		for(int i=0;i<n;i++)
		for(int j=0;j<=i*10;j++)
		for(int k=0;k<=i*10;k++)
		if(dp[i][j][k]!=-1)
		{
			for(int l=0;l<t[i];l++)
			{
				int tj=j+a[i][l];
				int tk=k+b[i][l];
				int cost=0;
				if(c[i][l]==1)cost=g[i];
				if(tj<=tk+1)
				dp[i+1][tj][tk]=max(dp[i+1][tj][tk],dp[i][j][k]+cost);
			}
		}
		int ret=0;
		for(int i=0;i<=n*10;i++)
		for(int j=0;j<=n*10;j++)
		ret=max(ret,dp[n][i][j]);
		printf("Case #%d: %d\n",ca,ret);
		cerr<<ca<<": "<<ret<<endl;
	}
	return 0;
}
