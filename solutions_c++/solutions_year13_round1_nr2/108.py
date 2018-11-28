// File Name: Blarge.cpp
// Author: YangYue
// Created Time: 六  4/27 10:33:51 2013
//headers 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<LL, LL>PLL;
typedef pair<LL,int>PLI;

#define lch(n) ((n<<1))
#define rch(n) ((n<<1)+1)
#define lowbit(i) (i&-i)
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define MP make_pair
#define PB push_back

const int MaxN = 20005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const LL LINF = 1000000000000000005ll;

int E, R, n;
int m, sink, source, et;
LL dist[MaxN], v[MaxN];
bool inque[MaxN];
struct Edge
{
	int u, v, f, w;
	Edge *next, *pre;
	Edge(){}
	Edge(int u, int v, int f, int w, Edge *next, Edge *pre)
		: u(u), v(v), f(f), w(w), next(next), pre(pre) {}
} *g[MaxN], *pre[MaxN], edge[MaxN*20];
void clear() { // 多cases 需注意!
	memset(g, 0, sizeof(g));
	memset(pre, 0, sizeof(pre));
	et = 0;
}
void Addedge(int u, int v, int f, int w)
{
	edge[et] = Edge(u, v, f, w, g[u], &edge[et+1]);
	edge[et+1] = Edge(v, u, 0, -w, g[v], &edge[et]);
	g[u] = &edge[et++];
	g[v] = &edge[et++];
}
queue < int > que;
bool SPFA()
{
	for (int i = 0; i <= sink; ++i) dist[i] = LINF; dist[source] = 0;
	for (int i = 0; i <= sink; ++i) inque[i] = 0;
	que.push(source); inque[source] = 1;
	while (!que.empty())
	{
		int u = que.front(); que.pop();
		for (Edge *p = g[u]; p; p = p->next)
			if (p->f > 0 && dist[p->v] > dist[u] + p->w)
			{
				dist[p->v] = dist[u] + p->w; pre[p->v] = p;
				if (!inque[p->v]) que.push(p->v), inque[p->v] = 1;
			}
		inque[u] = 0;
	}
	return dist[sink] < LINF;
}
LL mincost()
{
	LL flow, ans = 0, f = 0;
	while (SPFA())
	{
		flow = INF;
		for (Edge *p = pre[sink]; p; p = pre[p->u]) flow = min(flow, (LL) p->f);
		for (Edge *p = pre[sink]; p; p = pre[p->u]) p->f -= flow, p->pre->f += flow;
		ans += flow * dist[sink];
		f += flow;
	}
	return ans;
}

void build() {
	clear();

	source = 0; sink = 2 * n + 1;
	for (int i = 1; i <= n; ++i) {
		if (i == 1) Addedge(source, i, E, 0);
		else {
			Addedge(i - 1 + n, i, E, 0);
		}
		Addedge(i, i + n, E, 0);
		Addedge(source, i + n, R, 0);
		Addedge(i, sink, E, -v[i]);
	}
}
int main()
{
	freopen("in","r",stdin);
	freopen("output","w",stdout);

	int cases; cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		printf("Case #%d: ", cas);
		cin >> E >> R >> n;
		for (int i = 1; i <= n; ++i) scanf("%lld",v+i);
		build();
		printf("%lld\n", -mincost());
	}

	return 0;
}

// hehe ~


