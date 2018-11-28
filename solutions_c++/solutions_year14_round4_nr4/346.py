#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
typedef pair<int,int> PII;

#define maxn 110
#define maxe 202020
int ch[maxn][30],p;
void ins(char *str)
{
	int id=0,t;
	for(int i=0;str[i];i++)
	{
		t=str[i]-'A';
		if(!ch[id][t])
			ch[id][t]=++p;
		id=ch[id][t];
	}
}
vector<int>g[1010];
int vis[1010],maxx,ret,n,m;
char ss[110][10000];
void dfs(int d)
{
	if(d==m)
	{
		for(int i=0;i<n;i++)g[i].clear();
		for(int i=0;i<m;i++)g[vis[i]].push_back(i);
		for(int i=0;i<n;i++)if(g[i].size()==0)return;
		int ans=0,i,j;
		for(i=0;i<n;i++)
		{
			int sz=g[i].size();
			p=0;
			memset(ch,0,sizeof(ch));
			for(j=0;j<sz;j++)
				ins(ss[g[i][j]]);
			ans+=p+1;
		}
		if(ans>maxx)
			maxx=ans,ret=1;
		else if(ans==maxx)
			ret++;
		return;
	}
	for(int i=0;i<n;i++)
	{
		vis[d]=i;
		dfs(d+1);
	}
}
int main()
{
	int i,j,ncase,tt=0;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		scanf("%d %d",&m,&n);
		for(i=0;i<m;i++)scanf("%s",ss[i]);
		maxx=-1;
		ret=0;
		dfs(0);
		printf("Case #%d: %d %d\n",++tt,maxx,ret);
	}
}
