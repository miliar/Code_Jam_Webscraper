#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <cassert>
#include <climits>
#include <list>
using namespace std;
bool board[2005][1005];
struct Edge {
	int a;
	int w;
	list<Edge>::iterator back;
};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
list<Edge>::iterator dad[100005];
list<Edge> adj[100005];
int W, H, B, src, sink, minf[100005];
bool used[100005];
const int INF = 1000000000;
int getNode(int x, int y, bool type) {
	return W * 2 * y + 2 * x + type;
}
void addEdge(int x, int y) {
	Edge ef = {y, 1}, eb = {x, 0};
	adj[x].push_back(ef);
	adj[y].push_back(eb);
	adj[x].rbegin()->back = --adj[y].end();
	adj[y].rbegin()->back = --adj[x].end();
}
int findpath() {
	memset(used, 0, sizeof(used));
	queue<int> Q;
	minf[src] = INF;
	used[src] = true;
	Q.push(src);
	while (!Q.empty()) {
		int v = Q.front();
		Q.pop();
		if (v == sink) break;
		for (auto i = adj[v].begin(); i != adj[v].end(); ++i)
			if (i->w > 0 && !used[i->a]) {
				minf[i->a] = min(minf[v], i->w);
				dad[i->a] = i;
				used[i->a] = true;
				Q.push(i->a);
			}
	}
	if (!used[sink]) return INF;
	for (int v = sink; v != src; v = dad[v]->back->a) {
		dad[v]->w -= minf[sink];
		dad[v]->back->w += minf[sink];
	}
	return minf[sink];
}
int main() {
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn) {
		scanf("%d%d%d", &W, &H, &B);
		memset(board, 0, sizeof(board));
		for (int i = 0; i < B; ++i) {
			int x0, y0, x1, y1;
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			for (int x = x0; x <= x1; ++x)
				for (int y = y0; y <= y1; ++y)
					board[y][x] = 1;
		}
		for (int y = 0; y < H; ++y)
			for (int x = 0; x < W; ++x) {
				adj[getNode(x, y, 0)].clear();
				adj[getNode(x, y, 1)].clear();
			}
		src = getNode(W - 1, H - 1, 1) + 1;
		sink = src + 1;
		adj[src].clear();
		adj[sink].clear();
		for (int y = 0; y < H; ++y)
			for (int x = 0; x < W; ++x) {
				if (board[y][x]) continue;
				addEdge(getNode(x, y, 0), getNode(x, y, 1));
				for (int d = 0; d < 4; ++d) {
					int ny = y + dy[d];
					int nx = x + dx[d];
					if (ny >= 0 && ny < H && nx >= 0 && nx < W && !board[ny][nx]) {
						addEdge(getNode(nx, ny, 1), getNode(x, y, 0));
						addEdge(getNode(x, y, 1), getNode(nx, ny, 0));
					}
				}
			}
		for (int x = 0; x < W; ++x) {
			addEdge(src, getNode(x, 0, 0));
			addEdge(getNode(x, H - 1, 1), sink);
		}
		int ans = 0;
		for (;;) {
			int flow = findpath();
			if (flow == INF) break;
			ans += flow;
		}
		printf("Case #%d: %d\n", cn, ans);
	}
}

