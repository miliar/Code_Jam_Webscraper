#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

//const int walk[4][2]={{-1,0},{0,1},{1,0},{0,-1}};

const int maxp=100*500*2+5, maxe=100*500*4*5+5;

int W, H, B, a[maxp], m, b[maxe], c[maxe], d[maxe], dist[maxp];
bool flag[105][505];

#define S 0
#define IN(x,y) ((x)*H+(y)+1)
#define OUT(x,y) ((x)*H+(y)+1+W*H)
#define T (W*H*2+1)

inline void ADD(int x, int y, int z)
{
	m++, b[m]=y, c[m]=a[x], a[x]=m, d[m]=z;
	m++, b[m]=x, c[m]=a[y], a[y]=m, d[m]=0;
}

void Bfs()
{
	int st, en;
	static int list[maxp];
	list[st=en=1];
	memset(dist,255,sizeof dist);
	dist[S]=0;
	while (st<=en)
	{
		int now(list[st]);
		for (int i=a[now];i;i=c[i]) if (d[i] && dist[b[i]]==-1)
		{
			dist[b[i]]=dist[now]+1;
			list[++en]=b[i];
		}
		st++;
	}
}

int Dfs(int x, int flow)
{
	if (x==T) return flow;
	int ret(0);
	for (int i=a[x];i;i=c[i]) if (d[i] && dist[b[i]]==dist[x]+1)
	{
		int tmp(Dfs(b[i],min(d[i],flow)));
		d[i]-=tmp, d[i^1]+=tmp;
		ret+=tmp, flow-=tmp;
		if (!flow) return ret;
	}
	dist[x]=-1;
	return ret;
}

int Work()
{
	int ret(0);
	while (true)
	{
		Bfs();
		if (dist[T]==-1) break;
		ret+=Dfs(S,0x7fffffff);
	}
	return ret;
}

int main()
{
	freopen("p3.in","r",stdin);
	freopen("p3.out","w",stdout);
	int TT;
	scanf("%d",&TT);
	for (int tt=1;tt<=TT;tt++)
	{
		scanf("%d%d%d",&W,&H,&B);
		memset(flag,0,sizeof flag);
		memset(a,0,sizeof a);
		m=1;
		for (int i=1;i<=B;i++)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int p=x1;p<=x2;p++)
				for (int q=y1;q<=y2;q++)
					flag[p][q]=true;
		}
		for (int i=0;i<W;i++)
			for (int j=0;j<H;j++) if (!flag[i][j])
			{
				ADD(IN(i,j),OUT(i,j),1);
				if (i && !flag[i-1][j]) ADD(OUT(i-1,j),IN(i,j),1), ADD(OUT(i,j),IN(i-1,j),1);
				if (j && !flag[i][j-1]) ADD(OUT(i,j-1),IN(i,j),1), ADD(OUT(i,j),IN(i,j-1),1);
			}
		for (int i=0;i<W;i++)
		{
			ADD(S,IN(i,0),1);
			ADD(OUT(i,H-1),T,1);
		}
		printf("Case #%d: %d\n",tt,Work());
	}
	return 0;
}

