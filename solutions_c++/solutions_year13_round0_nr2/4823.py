#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <string>
using namespace std;
#define LL long long
#define maxn 210
#define maxe 101010
#define INF 1e40
#define fi first
#define se second
#define mp make_pair
#define pi acos(-1.0)
int n,m,r[maxn],c[maxn];
vector<int>g[maxn];

int jud()
{
	int i,j;
	memset(r,0,sizeof(r));
	memset(c,0,sizeof(c));
	for(i=100;i>0;i--)
	{
		int sz=g[i].size();
		for(j=0;j<sz;j+=2)
			if(r[g[i][j]]&&c[g[i][j+1]])
				return false;
		for(j=0;j<sz;j+=2)
			r[g[i][j]]=c[g[i][j+1]]=1;
	}
	return true;
}

int main()
{
	int i,j,tt=0,ncase,v;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		for(i=1;i<=100;i++)g[i].clear();
		scanf("%d %d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				scanf("%d",&v);
				g[v].push_back(i);
				g[v].push_back(j);
			}
		if(jud())
			printf("Case #%d: YES\n",++tt);
		else
			printf("Case #%d: NO\n",++tt);
	}
}
