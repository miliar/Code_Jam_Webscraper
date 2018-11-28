#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

const int Maxw = 102;
const int Maxh = 505;
const int Maxn = 2 + 2 * Maxw * Maxh;
const int Maxd = 4;
const int dy[Maxd] = {-1, 0, 1, 0};
const int dx[Maxd] = {0, -1, 0, 1};

struct edge {
	int a, b, f, c;
	edge(int a = 0, int b = 0, int f = 0, int c = 0):
			a(a), b(b), f(f), c(c) {}
};

int t;
int w, h, b;
bool taken[Maxw][Maxh];
vector <edge> E;
vector <int> neigh[Maxn];
int N;
bool flow[Maxn];
int par[Maxn];
int res;

int getIn(int x, int y) { return x * h + y + 1; }

int getOut(int x, int y) { return w * h + getIn(x, y); }

void addEdge(int a, int b)
{
	neigh[a].push_back(E.size());
	E.push_back(edge(a, b, 0, 1));
	neigh[b].push_back(E.size());
	E.push_back(edge(b, a, 0, 0));
}

int getFlow()
{
	fill(flow, flow + N, false); flow[0] = true;
	priority_queue <int> Q; Q.push(0);
	int v;
	while (!Q.empty()) {
		v = Q.top(); Q.pop();
		if (v == N - 1) break;
		for (int i = 0; i < neigh[v].size(); i++) {
			int e = neigh[v][i];
			if (E[e].f < E[e].c && !flow[E[e].b]) {
				flow[E[e].b] = true; par[E[e].b] = e;
				Q.push(E[e].b);
			}
		}
	}
	if (v != N - 1) return 0;
	while (v) {
		int e = par[v];
		E[e].f++; E[e ^ 1].f--;
		v = E[e].a;
	}
	return 1;
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &w, &h, &b);
		for (int i = 0; i < w; i++)
			for (int j = 0; j < h; j++)
				taken[i][j] = false;
		while (b--) {
			int x0, y0, x1, y1; scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
			for (int i = x0; i <= x1; i++)
				for (int j = y0; j <= y1; j++)
					taken[i][j] = true;
		}
		N = 2 + 2 * w * h;
		E.clear();
		for (int i = 0; i < N; i++)
			neigh[i].clear();
		for (int i = 0; i < w; i++)
			for (int j = 0; j < h; j++) if (!taken[i][j]) {
				int myin = getIn(i, j), myout = getOut(i, j);
				if (j == 0) addEdge(0, myin);
				for (int d = 0; d < Maxd; d++) {
					int ni = i + dy[d], nj = j + dx[d];
					if (0 <= ni && ni < w && 0 <= nj && nj < h && !taken[ni][nj])
						addEdge(myout, getIn(ni, nj));
				}
				addEdge(myin, myout);
				if (j == h - 1) addEdge(myout, N - 1);
			}
		res = 0;
		while (getFlow()) res++;
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}