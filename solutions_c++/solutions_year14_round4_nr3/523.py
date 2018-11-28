#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
struct edge{
	int u, v, cap, next;
}E[1000000];
int n, e, last[200000], p[200000], q[200000], f, l;
int W, H, B;
bool g[512][128];
int nr, nc, dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
bool getPath(int src, int sink){
	q[f = l = 0] = src;
	for (int i = 0; i<n; ++i)
		p[i] = -1;
	p[src] = src;
	while (f <= l){
		src = q[f];
		++f;
		for (int e = last[src]; e != -1; e = E[e].next)
		if (p[E[e].v] == -1 && E[e].cap>0){
			p[E[e].v] = e;
			if (E[e].v == sink)
				return true;
			q[++l] = E[e].v;
		}
	}
	return false;
}
int maxFlow(int src, int sink){
	int MaxFlow = 0;
	int flow;
	while (getPath(src, sink)){
		flow = (1 << 29) - 1;
		for (int c = sink; c != src; c = E[p[c]].u)
			flow = min(flow, E[p[c]].cap);
		for (int c = sink; c != src; c = E[p[c]].u){
			E[p[c]].cap -= flow;
			E[p[c] ^ 1].cap += flow;
		}
		MaxFlow += flow;
	}
	return MaxFlow;
}
void addEdge(int a, int b, int c){
	E[e].u = a; E[e].v = b; E[e].cap = c; E[e].next = last[a];
	last[a] = e++;
	E[e].u = b; E[e].v = a; E[e].cap = 0; E[e].next = last[b];
	last[b] = e++;
}
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; ++T){
		printf("Case #%d: ", T);
		memset(g, 0, sizeof(g));
		scanf("%d%d%d", &W, &H, &B);
		n = W*H * 2 + 2;
		int src = n - 2;
		int sink = n - 1;
		int N = W*H;
		e = 0;
		memset(last, -1, sizeof(last));
		int x1, x2, y1, y2;
		for (int i = 0; i < B; ++i){
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = y1; i <= y2;++i)
				for (int j = x1; j <= x2; ++j)
					g[i][j] = true;
		}
		for (int i = 0; i < N; ++i)
			addEdge(i, i + N, 1);
		for (int i = 0; i < H;++i)
		for (int j = 0; j < W;++j)
		if (!g[i][j]){
			for (int k = 0; k < 4; ++k){
				nr = i + dr[k];
				nc = j + dc[k];
				if (nr < 0 || nr == H || nc < 0 || nc == W || g[nr][nc])
					continue;
				addEdge(i*W + j + N, nr*W + nc, 1);
			}
		}
		for (int i = 0; i < W; ++i){
			if (!g[0][i])
				addEdge(i + N, sink, 1);
			if (!g[H - 1][i])
				addEdge(src, (H - 1)*W + i, 1);
		}
		printf("%d\n", maxFlow(src, sink));
	}
	return 0;
}