#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

#define INF 2000000000

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

const int MAXN = 550;
bool grid[MAXN][MAXN];
int mx[] = {-1, 0, 0, 1};
int my[] = {0, -1, 1, 0};

const int maxnodes = 2 * MAXN * MAXN;

int nodes = maxnodes, src, dest;
int dist[maxnodes], q[maxnodes], work[maxnodes];

struct Edge {
  int to, rev;
  int f, cap;
};

vector<Edge> g[maxnodes];

// Adds bidirectional edge
void addEdge(int s, int t, int cap){
//	cout << s << ' ' << t << ' ' << cap << endl;
  Edge a = {t, g[t].size(), 0, cap};
  Edge b = {s, g[s].size(), 0, 0};
  g[s].push_back(a);
  g[t].push_back(b);
}

bool dinic_bfs() {
  fill(dist, dist + nodes, -1);
  dist[src] = 0;
  int qt = 0;
  q[qt++] = src;
  for (int qh = 0; qh < qt; qh++) {
    int u = q[qh];
    for (int j = 0; j < (int) g[u].size(); j++) {
      Edge &e = g[u][j];
      int v = e.to;
      if (dist[v] < 0 && e.f < e.cap) {
        dist[v] = dist[u] + 1;
        q[qt++] = v;
      }
    }
  }
  return dist[dest] >= 0;
}

int dinic_dfs(int u, int f) {
  if (u == dest)
    return f;
  for (int &i = work[u]; i < (int) g[u].size(); i++) {
    Edge &e = g[u][i];
    if (e.cap <= e.f) continue;
    int v = e.to;
    if (dist[v] == dist[u] + 1) {
      int df = dinic_dfs(v, min(f, e.cap - e.f));
      if (df > 0) {
        e.f += df;
        g[v][e.rev].f -= df;
        return df;
      }
    }
  }
  return 0;
}

int maxFlow(int _src, int _dest) {
  src = _src;
  dest = _dest;
  int result = 0;
  while (dinic_bfs()) {
    fill(work, work + nodes, 0);
    while (int delta = dinic_dfs(src, 1000000000))
      result += delta;
  }
  return result;
}

void clear() {
	forn(i, maxnodes) {
		g[i].clear();
	}
}

int getFirst(int x, int y, int w, int h) {
	 return 2 * (y * w + x) + 1;
}

int getSecond(int x, int y, int w, int h) {
	 return 2 * (y * w + x) + 2;
}

void solve() {
	int w, h, b;
	scanf("%d %d %d", &w, &h, &b);
	forn(x, w) {
		forn(y, h) {
			grid[x][y] = false;
		}
	}
	forn(i, b) {
		int x0, y0, x1, y1;
		scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
		for (int x = x0; x <= x1; ++x) {
			for (int y = y0; y <= y1; ++y) {
				grid[x][y] = true;
			}
		}
	}
	clear();
	int sv = 0, fv = 2 * w * h + 1;
	forn(x, w) {
		if (!grid[x][0]) {
			addEdge(sv, getFirst(x, 0, w, h), 1);
		}
		if (!grid[x][h - 1]) {
			addEdge(getSecond(x, h - 1, w, h), fv, 1);
		}
	}
	forn(x, w) {
	forn(y, h) if (!grid[x][y]) {
		addEdge(getFirst(x, y, w, h), getSecond(x, y, w, h), 1);
		forn(k, 4) {
			int cx = x + mx[k];
			int cy = y + my[k];
			if (cx < 0 || cx >= w) {
				continue;
			}
			if (cy < 0 || cy >= h) {
				continue;
			}
			if (grid[cx][cy]) {
				continue;
			}
			addEdge(getSecond(x, y, w, h), getFirst(cx, cy, w, h), 1);
		}
	}
	}
	printf("%d\n", maxFlow(sv, fv));
}

int main(int argc, char **argv) {
//	freopen("input.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int tt;
	scanf("%d\n", &tt);
	forn(t, tt) {
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}
