#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long LL;
const int V=2100;
const int En=2*V*V;
struct Edge
{
	int num,ne;
}e[En];
int p[V],dg[V],K;
void add(int x,int y)
{
	e[K].num=y;dg[y]++;
	e[K].ne=p[x];p[x]=K++;
}
int T,n,a[V],b[V],pos[V],ret[V],vis[V];
int main()
{
    freopen("C-large.in.txt","r",stdin);
    freopen("C-large.out.txt","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)p[i]=-1;K=0;
		memset(dg,0,sizeof(dg));
		for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
		for(int i=0;i<n;i++)
            scanf("%d",&b[i]);
		memset(pos,-1,sizeof(pos));
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<i;j++)
                if(a[j]>=a[i])add(i,j);
			if(a[i]!=1)
			{
				add(pos[a[i]-1],i);
			}
			pos[a[i]]=i;
		}
		memset(pos,-1,sizeof(pos));
		for(int i=n-1;i>=0;i--)
		{
			for(int j=i+1;j<n;j++)
                if(b[j]>=b[i])add(i,j);
			if(b[i]!=1)
			{
				add(pos[b[i]-1],i);
			}
			pos[b[i]]=i;
		}
		memset(vis,0,sizeof(vis));
		for(int step=1;step<=n;step++)
		{
			int id=-1;
			for(int i=0;i<n;i++)
                if(!vis[i]&&dg[i]==0)
                {id=i;break;}
			if(id==-1)while(1);
			ret[id]=step;vis[id]=1;
			for(int i=p[id];i!=-1;i=e[i].ne)
			{
				int v=e[i].num;
				dg[v]--;
			}
		}
		printf("Case #%d:",ca);
		for(int i=0;i<n;i++)printf(" %d",ret[i]);
		puts("");
	}
}
