#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
bool incirle[1010];
bool vis[1010];
int to[1010];
set<int>ooxx;
int dp[1010];
int get(int x)
{
	ooxx.clear();
	while(1)
	{
		vis[x]=true;
		ooxx.insert(x);
		if(ooxx.find(to[x]) != ooxx.end())
			return to[x];
		x=to[x];
	}
}
int end[1010];
int pp[1010];
int qq;
int dis[1010][1010];
int ans;
bool ok[1010][1010];
void mark_circle(int x)
{
	qq=0;
	while(dp[x] == -1)
	{
		incirle[x]=true;
		end[x]=x;
		pp[qq++]=x;
		dp[x]=0;
		x=to[x];
	}
	ans=max(ans,qq);
	if(qq == 2)
		ok[x][to[x]]=ok[to[x]][x]=true;
}
int dfs(int x)
{
	if(dp[x] != -1)
		return dp[x];
	dp[x]=dfs(to[x])+1;
	end[x]=end[to[x]];
	return dp[x];
}
int big[1010][1010];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		ans=0;
		int n;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&to[i]);
		memset(vis,false,sizeof(vis));
		memset(incirle,false,sizeof(incirle));
		memset(dp,-1,sizeof(dp));
		memset(ok,false,sizeof(ok));
		memset(end,-1,sizeof(end));
		for(int i=1;i<=n;i++)
			if(!vis[i])
			{
				int x=get(i);
				if(incirle[x])
					continue;
				mark_circle(x);
			}
		for(int i=1;i<=n;i++)
			if(dp[i] == -1)
				dfs(i);
//		for(int i=1;i<=n;i++)
//			printf("%d ",dp[i]);
//		printf("\n");
//		for(int i=1;i<=n;i++)
//			printf("%d ",end[i]);
//		printf("\n");
//		for(int i=1;i<=n;i++)
//		{
//			for(int j=1;j<=n;j++)
//				printf("%d ",dis[i][j]);
//			printf("\n");
//		}
		memset(big,0,sizeof(big));
		for(int i=1;i<=n;i++)
			for(int j=i+1;j<=n;j++)
			{
				int x=end[i];
				int y=end[j];
				if(ok[x][y])
					big[y][x]=big[x][y]=max(big[x][y],dp[i]+dp[j]+2);
			}
		int l=0;
		for(int i=1;i<=n;i++)
			for(int j=i+1;j<=n;j++)
				if(ok[i][j])
					l+=big[i][j];
		printf("Case #%d: %d\n",cc,max(ans,l));
	}
    return 0;
}
/*
4
4
2 3 4 1
4
3 3 4 1
4
3 3 4 3
10
7 8 10 10 9 2 9 6 3 3

1
4
3 3 4 1

 */
