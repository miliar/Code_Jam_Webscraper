#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <cassert>

using namespace std;

const long long MOD = 1000002013;
const int MAXN = 2100;
const int MAXM = 2500000;
const int INF = 1e9 + 100;

struct segment {
	int l, r, p, id;
	segment(int id, int l, int r, int p): id(id), l(l), r(r), p(p) {}
	segment() {}
};

int col, n, m, sz;
long long resultCost;
vector<segment> s;
vector<int> color;

int head[MAXN], next[MAXM], c[MAXM], maxc[MAXM], cost[MAXM], from[MAXM], to[MAXM];
int used[MAXN], p[MAXN], saveEdge[MAXN][MAXN], d[MAXN], phi[MAXN];

void addEdge(int u, int v, int flow, int price) {
	//fprintf(stderr, "add edge %d->%d, flow = %d, price = %d\n", u, v, flow, price);
	c[sz] = maxc[sz] = flow;
	from[sz] = u;
	to[sz] = v;
	cost[sz] = price;
	next[sz] = head[u];
	head[u] = sz;
	sz++;
	c[sz] = maxc[sz] = 0;
	from[sz] = v;
	to[sz] = u;
	cost[sz] = -price;
	next[sz] = head[v];
	head[v] = sz;
	sz++;
}

void dijkstra(int source) {
	memset(used, 0, sizeof(used));
	memset(p, -1, sizeof(p));
	fill(d, d + 2 * m + 2, INF);
	d[source] = 0;
	while (true) {
		int j = -1;
		for (int i = 0; i <= 2 * m + 1; ++i) {
			if (!used[i] && d[i] < INF && (j < 0 || d[i] < d[j])) {
				j = i;
			}
		}
		if (j < 0) {
			break;
		}
		used[j] = 1;
		for (int i = head[j]; i != -1; i = next[i]) {
			if (c[i] > 0) {
				int v = to[i];
				if (d[j] + cost[i] + phi[j] - phi[v] < d[v]) {
					d[v] = d[j] + cost[i] + phi[j] - phi[v];
					p[v] = i;
				}
			}
		}
	}
}

void minCostFlow(int source, int sink) {
	memset(phi, 0, sizeof(phi));
	int resultFlow = 0;
	while (true) {
		dijkstra(source);
		if (d[sink] == INF) {
			break;
		}
		for (int i = 0; i <= 2 * m + 1; ++i) {
			phi[i] += d[i] != INF ? d[i] : d[sink];
		}
		int flow = INF;
		for (int i = p[sink]; i != -1; i = p[from[i]]) {
			flow = min(flow, c[i]);
		}
		for (int i = p[sink]; i != -1; i = p[from[i]]) {
			c[i] -= flow;
			c[i ^ 1] += flow;
			resultCost += 1LL * flow * cost[i] % MOD;
			resultCost %= MOD;
		}
		resultFlow += flow;
	}
}

bool is_inter(const segment &a, const segment &b) {
	if (b.l <= a.l && a.l <= b.r) {
		return true;
	}
	if (b.l <= a.r && a.r <= b.r) {
		return true;
	}
	if (a.l <= b.l && b.l <= a.r) {
		return true;
	}
	if (a.l <= b.r && b.r <= a.r) {
		return true;
	}
	return false;
}

long long getcost(int m) {
	return (1LL * m * n - 1LL * m * (m - 1) / 2) % MOD;
}

int dfs(int v) {
	color[v] = col;
	for (int i = 0; i < m; ++i) {
		if (color[i] == 0 && is_inter(s[v], s[i])) {
			dfs(i);
		}
	}
}

void solve() {
	memset(head, -1, sizeof(head));
	sz = 0;
	resultCost = 0;
	long long old = 0;
	scanf("%d%d\n", &n, &m);
	s.resize(m);
	for (int i = 0; i < m; ++i) {
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		old += 1LL * c * getcost(b - a) % MOD;
		old %= MOD;
		s[i] = segment(i, a, b, c);
	}
	
	color.assign(m, 0);
	col = 1;
	for (int i = 0; i < m; ++i) {
		if (color[i] == 0) {
			dfs(i);
			col++;
		}
	}
	for (int i = 0; i < m; ++i) {
		addEdge(0, i + 1, s[i].p, 0);
		addEdge(m + i + 1, 2 * m + 1, s[i].p, 0);
	}
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < m; ++j) {
			if (color[i] == color[j] && s[j].r >= s[i].l) {
				addEdge(i + 1, m + j + 1, INF, getcost(s[j].r - s[i].l));
			}
		}
	}
	minCostFlow(0, 2 * m + 1);
	resultCost %= MOD;
	long long res = (old - resultCost + MOD) % MOD;
	cout << res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		fprintf(stderr, "Case %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	return 0;
}