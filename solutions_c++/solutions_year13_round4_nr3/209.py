#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define eps 1e-8
#define pi acos(-1.0)
bool vis[110];
int a[2010];
int b[2010];
int aa[2010];
int bb[2010];
int pp[2010];
int s[2010];
int n;
bool ok()
{
	for(int i=0;i<n;i++)if(vis[i])
	{
		aa[i]=1;
		for(int j=0;j<i;j++)if(vis[j])
			if(s[i] > s[j])
				aa[i]=max(aa[i],aa[j]+1);
	}
	for(int i=n-1;i>=0;i--)if(vis[i])
	{
		bb[i]=1;
		for(int j=n-1;j>i;j--)if(vis[j])
			if(s[i] > s[j])
				bb[i]=max(bb[i],bb[j]+1);
	}
	for(int i=0;i<n;i++)if(vis[i])
	{
		if(a[i] != aa[i])
			return false;
		if(b[i] != bb[i])
			return false;
	}
	return true;
}
bool dfs(int dep)
{
	if(dep == n)
		return true;
	for(int i=0;i<n;i++)
	{
		if(vis[i])
			continue;
		s[i]=dep;
		vis[i]=true;
		if(ok())
		{
			if(dfs(dep+1))
				return true;
		}
		vis[i]=false;
	}
	return false;
}
int main()
{
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%d",&b[i]);
		memset(vis,false,sizeof(vis));
		dfs(0);
		printf("Case #%d:",cc);
		for(int i=0;i<n;i++)
			if(!vis[i])
				s[i]=-1;
		for(int i=0;i<n;i++)
			printf(" %d",s[i]+1);
		printf("\n");
	}
	return 0;
}
/*
2
1
1
1
8
1 2 1 3 3 1 4 1
4 4 3 4 3 2 2 1

10
1 1 1 1 1 1 1 1 1 1
10 9 8 7 6 5 4 3 2 1
 */
