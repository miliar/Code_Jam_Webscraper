#pragma comment(linker,"/stack:256000000")

#include <cmath> 
#include <ctime> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <cstring> 
#include <cstdlib> 
#include <queue> 
#include <cstdio> 
#include <cfloat>
#include <cassert>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

const int MAXN = 100100; // число вершин
const int INF = 1000000000; // константа-бесконечность
 
struct edge {
	int a, b, cap, flow;
};
 
int n, s, t, d[MAXN], ptr[MAXN], q[MAXN];
vector<edge> e;
vector<int> g[MAXN];
 
void add_edge (int a, int b, int cap) {
	edge e1 = { a, b, cap, 0 };
	edge e2 = { b, a, 0, 0 };
	g[a].push_back ((int) e.size());
	e.push_back (e1);
	g[b].push_back ((int) e.size());
	e.push_back (e2);
}
 
bool bfs() {
	int qh=0, qt=0;
	q[qt++] = s;
	memset (d, -1, n * sizeof d[0]);
	d[s] = 0;
	while (qh < qt && d[t] == -1) {
		int v = q[qh++];
		for (size_t i=0; i<g[v].size(); ++i) {
			int id = g[v][i],
				to = e[id].b;
			if (d[to] == -1 && e[id].flow < e[id].cap) {
				q[qt++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[t] != -1;
}
 
int dfs (int v, int flow) {
	if (!flow)  return 0;
	if (v == t)  return flow;
	for (; ptr[v]<(int)g[v].size(); ++ptr[v]) {
		int id = g[v][ptr[v]],
			to = e[id].b;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs (to, min (flow, e[id].cap - e[id].flow));
		if (pushed) {
			e[id].flow += pushed;
			e[id^1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}
 
int dinic() {
	int flow = 0;
	for (;;) {
		if (!bfs())  break;
		memset (ptr, 0, n * sizeof ptr[0]);
		while (int pushed = dfs (s, INF))
			flow += pushed;
	}
	return flow;
}

bool u[505][105];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void solve() {
	::n = 0, ::s = 0, ::t = 0;
	memset(d, 0, sizeof(d));
	memset(ptr, 0, sizeof(ptr));
	memset(q, 0, sizeof(q));
	e.clear();
	REP(i, MAXN) g[i].clear();
	memset(u, 0, sizeof(u));
	int w, h, b;
	cin >> w >> h >> b;
	REP(i, b) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int j = x1; j <= x2; j++) {
			for (int k = y1; k <= y2; k++) {
				u[k][j] = 1;
			}
		}
	}
	::n = 2 * w * h + 2;
	::s = ::n - 2;
	::t = ::n - 1;
	REP(i, w) {
		if (!u[0][i]) {
			add_edge(::s, i, 1);
		}
	}
	REP(i, w) {
		if (!u[h - 1][i]) {
			add_edge(w * h + (h - 1) * w + i, ::t, 1);
		}
	}
	REP(i, h) {
		REP(j, w) {
			if (u[i][j]) continue;
			add_edge(i * w + j, w * h + i * w + j, 1);
			REP(k, 4) {
				int ni = i + dx[k];
				int nj = j + dy[k];
				if (0 <= ni && ni < h && 0 <= nj && nj < w && !u[ni][nj]) {
					add_edge(w * h + i * w + j, ni * w + nj, 1);
				}
			}
		}
	}
	cout << dinic();
}	

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int tst = 1; tst <= T; tst++) {
		cerr << tst << endl;
		cout << "Case #" << tst << ": ";
		solve();
		cout << endl;
	}
	return 0;
}