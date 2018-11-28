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
pair<int,int>pp[100010];
int qq;
char g[110][110];
int num[1<<16];
int n;
int id[110];
bool used[110];
bool dfs(int at)
{
	if(at == n)
		return true;
	int now=id[at];
	bool exist=false;
	for(int i=0;i<n;i++)
	{
		if(used[i])
			continue;
		if(g[now][i] == '0')
			continue;
		used[i]=true;
		exist=true;
		if(!dfs(at+1))
			return false;
		used[i]=false;
	}
	if(!exist)
		return false;
	return true;
}
bool ok()
{
	for(int i=0;i<n;i++)
		id[i]=i;
	do
	{
		for(int i=0;i<n;i++)
			used[i]=false;
		if(!dfs(0))
			return false;
	}while(next_permutation(id,id+n));
	return true;
}
int main()
{
	for(int mask=0;mask<(1<<16);mask++)
	{
		num[mask]=0;
		for(int i=0;i<16;i++)
			if(mask&(1<<i))
				num[mask]++;
	}
	freopen("D-small-attempt0.in","r",stdin);
//	freopen("A.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%s",g[i]);
		qq=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(g[i][j] == '0')
					pp[qq++]=mp(i,j);
		int ans=0xfffffff;
		for(int mask=0;mask<(1<<qq);mask++)
		{
			if(num[mask] >= ans)
				continue;
			for(int i=0;i<qq;i++)
			{
				if(mask&(1<<i))
					g[pp[i].X][pp[i].Y]='1';
				else
					g[pp[i].X][pp[i].Y]='0';
			}
			if(ok())
				ans=min(ans,num[mask]);
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
/*
5
2
11
10
2
10
00
3
000
000
000
1
1
3
000
110
000

 */
