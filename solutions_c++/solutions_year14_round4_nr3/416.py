#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>
using namespace std;
const int maxn=1 << 20;
//{20 Maximum Flow -- Edmonds-Karp in Link
//Add a reversal edge with capacity 0 for each edge in a directed graph.
//edge::r=Reversal edge's ID
struct edge {int v,c,f,r,next;};
int EdmondsKarp(int g[],edge e[],int n,int src,int dst)
{
	static int d[maxn]={},p[maxn],h[maxn],r[maxn],c[maxn]={};
	std::fill(d, d + n, 0);
	std::fill(c, c + n, 0);
	int flow=0,delta=INT_MAX,v=src;
	c[src]=n;
	memcpy(r,g,sizeof(r));
	p[src]=-1;
	while(d[src]<n)
	{

		bool flag=true;;
		h[v]=delta;
		for(int i=r[v];i!=-1;i=e[i].next)
			if(e[i].c>e[i].f&&d[v]==d[e[i].v]+1)
			{
				if(delta>e[i].c-e[i].f) delta=e[i].c-e[i].f;
				flag=false;
				r[v]=i;
				p[e[i].v]=e[i].r;
				v=e[i].v;
				break;
			}
		if(flag)
		{
			int t=n-1;
			for(int i=g[v];i!=-1;i=e[i].next)
				if(t>d[e[i].v]&&e[i].f<e[i].c) {t=d[e[i].v];r[v]=i;}
			if(--c[d[v]]==0) break;
			d[v]=t+1;
			c[d[v]]++;
			if(p[v]!=-1) {v=e[p[v]].v;delta=h[v];}
		}
		else if(v==dst)
		{
			flow+=delta;
			while(p[v]!=-1)
			{
				e[p[v]].f-=delta;
				e[e[p[v]].r].f+=delta;
				v=e[p[v]].v;
			}
			delta=INT_MAX;
		}
	}
	return flow;
}
//}

int X0[1000], Y0[1000], X1[1000], Y1[1000];
int W, H, B;

int g[maxn];
edge e[510 * 110 * 100];
int en;

void AddEdge(int g[],edge e[],int &m,int u,int v,int c)
{
	e[m].f=0;e[m].v=v;e[m].c=c;e[m].r=m+1;e[m].next=g[u];g[u]=m++;
	e[m].f=0;e[m].v=u;e[m].c=0;e[m].r=m-1;e[m].next=g[v];g[v]=m++;
}

int id(int y, int x, int out)
{
	return out * W * H + y * W + x;
}

int solve()
{
	static bool mp[500][100];
	memset(mp, 0, sizeof(mp));
	for (int i = 0; i < B; ++i)
	{
		for (int y = Y0[i]; y <= Y1[i]; ++y)
		{
			for (int x = X0[i]; x <= X1[i]; ++x)
			{
				mp[y][x] = true;
			}
		}
	}

//	for (int y = 0; y < H; ++y)
//	{
//		for (int x = 0; x < W; ++x) putchar(mp[y][x] ? '#' : '.');
//		puts("");
//	}

	int src = W * H * 2, dst = src + 1;
	int n = dst + 1;
	std::fill(g, g + n, -1);
	en = 0;

	for (int i = 0; i < W; ++i)
	{
		AddEdge(g, e, en, src, id(0, i, 0), 1);
	}
	for (int i = 0; i < W; ++i)
	{
		AddEdge(g, e, en, id(H - 1, i, 1), dst, 1);
	}
	for (int y = 0; y < H; ++y)
	{
		for (int x = 0; x < W; ++x)
		{
			if (mp[y][x]) continue;
			AddEdge(g, e, en, id(y, x, 0), id(y, x, 1), 1);
			if (x + 1 < W && !mp[y][x + 1])
			{
//				printf("A %d %d\n", x, y);
				AddEdge(g, e, en, id(y, x, 1), id(y, x + 1, 0), 1);
			}
			if (y + 1 < H && !mp[y + 1][x])
			{
//				printf("B %d %d\n", x, y);
				AddEdge(g, e, en, id(y, x, 1), id(y + 1, x, 0), 1);
			}
			if (x - 1 >= 0 && !mp[y][x - 1])
			{
				AddEdge(g, e, en, id(y, x, 1), id(y, x - 1, 0), 1);
			}
			if (y - 1 >= 0 && !mp[y - 1][x])
			{
//				printf("B %d %d\n", x, y);
				AddEdge(g, e, en, id(y, x, 1), id(y - 1, x, 0), 1);
			}
		}
	}
	int ans = EdmondsKarp(g, e, n, src, dst);
//	printf("en=%d\n", en);
	//for (int i = 0; i < en; ++i) printf("%d: v=%d c=%d f=%d\n", i, e[i].v, e[i].c, e[i].f);
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d%d%d", &W, &H, &B);
		for (int i = 0; i < B; ++i)
		{
			scanf("%d%d%d%d", &X0[i], &Y0[i], &X1[i], &Y1[i]);
		}
		printf("Case #%d: %d\n", cs, solve());
	}
	return 0;
}
