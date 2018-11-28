//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define NODE 1000000
#define EDGE 10000000
#define INFI 87654321
struct edge {
	int next, node, w;
} e[EDGE << 1 | 1];
int head[NODE + 1], tot = 1;

void addedge(int a, int b, int w) {
	e[++tot].next = head[a];
	head[a] = tot, e[tot].node = b, e[tot].w = w;
	e[++tot].next = head[b];
	head[b] = tot, e[tot].node = a, e[tot].w = 0;
//	cerr << a << " " << b << " " << w << endl;
}

int S, T, d[NODE + 1], q[NODE + 1], M = 0;

bool bfs() {
	int h = 0, t = 0;
	for (int i = S; i <= T; ++i) d[i] = 0;
	d[S] = 1, q[t++] = S;
	while (h < t) {
		int cur = q[h++];
		for (int i = head[cur]; i; i = e[i].next) {
			if (!e[i].w) continue;
			int node = e[i].node;
			if (d[node]) continue;
			d[node] = d[cur] + 1;
			q[t++] = node;
		}
	}
	return d[T] != 0;
}

int dfs(int x, int inflow) {
	if (x == T) return inflow;
	int ret = inflow, flow;
	for (int i = head[x]; i; i = e[i].next) {
		if (!e[i].w) continue;
		int node = e[i].node;
		if (d[node] != d[x] + 1) continue;
		flow = dfs(node, min(e[i].w, ret));
		if (!flow) continue;
		ret -= flow, e[i].w -= flow, e[i ^ 1].w += flow;
		if (!ret) break;
	}
	if (ret == inflow) d[x] = -1;
	return inflow - ret;
}

int maxFlow() {
	int ret = 0;
	while (bfs())
		ret += dfs(S, INFI);
	return ret;
}

#define N 500
int Cases, Case = 0, n, m, k;
bool v[N + 1][N + 1];

int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

inline int node(int x, int y, int z) {
	return (x - 1) * m + y + n * m * z;
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	ios::sync_with_stdio(false);
	cin >> Cases;
	while (Cases--) {
		cin >> n >> m >> k;
		memset(v, 0, sizeof v);
		memset(head, 0, sizeof head);
		tot = 1;
		for (int i = 1; i <= k; ++i) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			++x1, ++y1, ++x2, ++y2;
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					v[x][y] = true;
		}
		for (int x = 1; x <= n; ++x)
			for (int y = 1; y <= m; ++y) {
				if (!v[x][y]) addedge(node(x, y, 0), node(x, y, 1), 1);
//				if (v[x][y]) continue;
				for (int d = 0; d < 2; ++d) {
					int nx = x + dir[d][0], ny = y + dir[d][1];
					if (nx > n || ny > m) continue;
//					if (!v[nx][ny]) {
						addedge(node(x, y, 1), node(nx, ny, 0), 1);
						addedge(node(nx, ny, 1), node(x, y, 0), 1);
//					}
				}
			}
		S = 0, T = n * m * 2 + 1;
		for (int i = 1; i <= n; ++i)
			if (!v[i][1]) addedge(S, node(i, 1, 0), 1);
		for (int i = 1; i <= n; ++i)
			if (!v[i][m]) addedge(node(i, m, 1), T, 1);
		
		int ans = maxFlow();
		cout << "Case #" << ++Case << ": " << ans << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
