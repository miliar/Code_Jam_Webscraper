#include <cmath>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
typedef pair<int,int> PII;

#define maxn 220000
#define maxe 1200000
#define INF 1<<30
#define LL long long
int n,m;
int f[maxe],cap[maxe];//flow[maxn][maxn];
int first[maxn],dis[maxn],gap[maxn],arc[maxn],Next[maxe],vv[maxe],pre[maxn],add,tot;
void adj(int u,int v,int ca)
{
	Next[add]=first[u]; vv[add]=v; cap[add]=ca; first[u]=add++;
    Next[add]=first[v]; vv[add]=u; cap[add]=0; first[v]=add++;
}
void adj1(int u,int v,int ca)
{
	Next[add]=first[u]; vv[add]=v; cap[add]=ca; first[u]=add++;
    Next[add]=first[v]; vv[add]=u; cap[add]=ca; first[v]=add++;
}
int q[maxn];
bool vis[maxn];
int sap(int s,int t,int n)
{
	int i,j,mindis,front=0,rear=1,u,v,e;
	int ans=0,low;
	bool found;

	memset(dis,0,sizeof(dis));
	memset(gap,0,sizeof(gap));
	memset(vis,0,sizeof(vis));
	memset(arc,0,sizeof(arc));

	q[0]=t;vis[t]=true;dis[t]=0;gap[0]=1;

	while(front<rear)
	{
		u=q[front++];e=first[u];

		while(e)
		{
			v=vv[e];

			if(!vis[v])
			{
				dis[v]=dis[u]+1;
				vis[v]=true;
				q[rear++]=v;
				gap[dis[v]]++;
				arc[v]=first[v];
			}

			e=Next[e];
		}
	}
	u=s;low=INF;pre[s]=s;//gap[s]=n;

	while(dis[s]<n)
	{
		found=false;

		for(int &e=arc[u];e;e=Next[e])if(dis[vv[e]]==dis[u]-1&&cap[e]>f[e])
		{
			found=true;v=vv[e];

			low=low<cap[e]-f[e]?low:cap[e]-f[e];
			pre[v]=u;u=v;

			if(u==t)
			{
				while(u-s)
				{
					u=pre[u];
					f[arc[u]]+=low;
					f[arc[u]^1]-=low;
				}
				ans+=low;low=INF;
			}
			break;
		}

		if(found)
			continue;

		mindis=n;
		for(int e=first[u];e;e=Next[e])
			if(mindis>dis[vv[e]]&&cap[e]>f[e])
			{
				mindis=dis[vv[j=e]];
				arc[u]=e;
			};

		gap[dis[u]]--;
		if(gap[dis[u]]==0)
			return ans;

		dis[u]=mindis+1;
		gap[dis[u]]++;

		u=pre[u];
	}
	return ans;
}

int g[110][510],w,h,k;
int ch(int x,int y)
{
	return x*h+y;
}
int dx[]={0,1,-1,0};
int dy[]={1,0,0,-1};
int main()
{
	int ncase,i,j,x,y,x0,x1,y0,y1,tt=0;
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	scanf("%d",&ncase);
	while(ncase--)
	{
		scanf("%d %d %d",&w,&h,&k);
		memset(g,0,sizeof(g));
		for(i=0;i<k;i++)
		{
			scanf("%d %d %d %d",&x0,&y0,&x1,&y1);
			for(x=x0;x<x1+1;x++)
				for(y=y0;y<y1+1;y++)
					g[x][y]=1;
		}
		memset(first,0,sizeof(first));add=2;
		memset(f,0,sizeof(f));
		for(i=0;i<w;i++)
			for(j=0;j<h;j++)if(!g[i][j])
			{
				adj1(ch(i,j)*2,ch(i,j)*2+1,1);
				for(int ii=0;ii<4;ii++)
				{
					int tx=i+dx[ii];
					int ty=j+dy[ii];
					if(tx<0||tx>=w||ty<0||ty>=h) continue;
					if(g[tx][ty]==1) continue;
					adj(ch(i,j)*2+1,ch(tx,ty)*2,1);
				}
			}
		int s=w*h*2+10,e=s+1;
		for(i=0;i<w;i++)if(!g[i][0])
			adj(s,ch(i,0)*2,1);
		for(i=0;i<w;i++)if(!g[i][h-1])
			adj(ch(i,h-1)*2+1,e,1);
		printf("Case #%d: %d\n",++tt,sap(s,e,e+1));
	}
	return 0;
}