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
const int oo=1000000000;
const int V=1020;
int tr[V],N;
void add(int k,int v)
{
	while(k<=N)
	{
		tr[k]+=v;
		k+=k&-k;
	}
}
int read(int k)
{
	int ret=0;
	while(k)
	{
		ret+=tr[k];
		k-=k&-k;
	}
	return ret;
}
struct Node
{
	int id,va;
}q[V];
bool cmp(Node x,Node y)
{
	return x.va<y.va;
}
int _,n,dp[V][V];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&q[i].va);
			q[i].id=i+1;
		}
		sort(q,q+n,cmp);
		for(int i=0;i<=n;i++)
		for(int j=0;j<=n;j++)
		dp[i][j]=oo;
		dp[0][0]=0;
		N=n;
		for(int i=0;i<=N;i++)tr[i]=0;
		for(int i=1;i<=N;i++)add(i,1);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			if(dp[i][j]!=oo)
			{
				 dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j]+read(q[i].id-1));
				 dp[i+1][j]=min(dp[i+1][j],dp[i][j]+read(N)-read(q[i].id));
			}
			add(q[i].id,-1);
		}
		int ret=oo;
		for(int i=0;i<=n;i++)ret=min(ret,dp[n][i]);
		cerr<<ca<<endl;
		printf("Case #%d: %d\n",ca,ret);
	}
	return 0;
}
