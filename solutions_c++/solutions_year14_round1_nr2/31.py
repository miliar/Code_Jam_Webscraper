#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define maxn 2010
struct Edge
{
	int v,next;
}edge[1000010];
int head[maxn];
int pos;
void insert(int x,int y)
{
	edge[pos].v=y;
	edge[pos].next=head[x];
	head[x]=pos++;
}
void change(int &x,int &y,int z)
{
	if(z < x)
	{
		y=x;
		x=z;
	}
	else if(z < y)
		y=z;
}
int du[maxn];
int dp[maxn];
int del[maxn];
void dfs(int now,int pre)
{
	int son;
	if(pre == -1)
		son=du[now];
	else
		son=du[now]-1;
	if(son == 0)
	{
		dp[now]=0;
		del[now]=1;
	}
	else if(son == 1)
	{
		del[now]=1;
		for(int i=head[now];i;i=edge[i].next)
		{
			int v=edge[i].v;
			if(v == pre)
				continue;
			dfs(v,now);
			del[now]+=del[v];
			dp[now]=del[v];
		}
	}
	else
	{
		del[now]=1;
		dp[now]=0;
		int x,y;
		x=y=10086;
		for(int i=head[now];i;i=edge[i].next)
		{
			int v=edge[i].v;
			if(v == pre)
				continue;
			dfs(v,now);
			del[now]+=del[v];
			dp[now]+=del[v];
			change(x,y,dp[v]-del[v]);
		}
		dp[now]=min(dp[now],dp[now]+x+y);
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		memset(head,0,sizeof(head));
		pos=1;
		memset(du,0,sizeof(du));
		int n;
		scanf("%d",&n);
		for(int i=1;i<n;i++)
		{
			int x,y;
			scanf("%d %d",&x,&y);
			insert(x,y);
			insert(y,x);
			du[x]++;
			du[y]++;
		}
		int ans=10086;
		for(int i=1;i<=n;i++)
		{
			dfs(i,-1);
			ans=min(ans,dp[i]);
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
/*
3
3
2 1
1 3
7
4 5
4 2
1 2
3 1
6 4
3 7
4
1 2
2 3
3 4

 */
