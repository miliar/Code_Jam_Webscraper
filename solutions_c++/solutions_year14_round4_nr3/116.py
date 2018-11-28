#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f;
const double eps = 1e-8, pi = acos(-1.0);

const int maxn = 1011, maxm = 1000001 * 4;
int w, h, b, tests;
struct rect {
	int x0, y0, x1, y1;
	void read() {
		scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
		++x0, ++y0, ++x1, ++y1;
	}
} r[maxn];

int __abs(int x) {
	return max(x, -x);
}

int ec, d[maxn];
struct edge_link {
	int v, w;
	edge_link *next;
} edge[maxm], *header[maxn];
struct item_t {
	int u, w;
	item_t(int tu, int tw) : u(tu), w(tw) { }
	bool operator<(const item_t &r) const {
		return w > r.w;
	}
};

void add(int u, int v, int w) {
	// printf("%d %d %d\n", u, v, w);
	edge[++ec].v = v, edge[ec].w = w, edge[ec].next = header[u], header[u] = &edge[ec];
}

int dijkstra(int s, int t) {
	priority_queue<item_t> pq;
	memset(d, 0x7f, sizeof(d));
	d[s] = 0, pq.push(item_t(s, 0));
	while (!pq.empty()) {
		item_t tp = pq.top();
		pq.pop();
		if (tp.w == d[tp.u]) {
			int u = tp.u, w = tp.w;
			if (u == t) {
				return d[t];
			} else {
				for (edge_link *e = header[u]; e != NULL; e = e->next) {
					if (w + e->w < d[e->v]) {
						d[e->v] = w + e->w;
						pq.push(item_t(e->v, d[e->v]));
					}
				}
			}
		}
	}
	return maxint;
}

bool in(int x, int l, int r) {
	return x >= l && x <= r;
}

int cal(int index1, int index2) {
	int dx1 = min(__abs(r[index1].x0 - r[index2].x1), __abs(r[index1].x1 - r[index2].x0));
	int dx2 = min(__abs(r[index1].x0 - r[index2].x0), __abs(r[index1].x1 - r[index2].x1));
	int dy1 = min(__abs(r[index1].y0 - r[index2].y1), __abs(r[index1].y1 - r[index2].y0));
	int dy2 = min(__abs(r[index1].y0 - r[index2].y0), __abs(r[index1].y1 - r[index2].y1));
	int dx = min(dx1, dx2), dy = min(dy1, dy2);

	if (in(r[index1].x0, r[index2].x0, r[index2].x1)) dx = 0;
	if (in(r[index1].x1, r[index2].x0, r[index2].x1)) dx = 0;
	swap(index1, index2);
	if (in(r[index1].x0, r[index2].x0, r[index2].x1)) dx = 0;
	if (in(r[index1].x1, r[index2].x0, r[index2].x1)) dx = 0;
	swap(index1, index2);

	if (in(r[index1].y0, r[index2].y0, r[index2].y1)) dy = 0;
	if (in(r[index1].y1, r[index2].y0, r[index2].y1)) dy = 0;
	swap(index1, index2);
	if (in(r[index1].y0, r[index2].y0, r[index2].y1)) dy = 0;
	if (in(r[index1].y1, r[index2].y0, r[index2].y1)) dy = 0;

	swap(index1, index2);

	if (dx == 0) dx = 1;
	if (dy == 0) dy = 1;
	return max(dx, dy)-1;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &tests);
	for (int tt = 1; tt <= tests; ++tt) {
		scanf("%d%d%d", &w, &h, &b);
		for (int i = 1; i <= b; ++i) {
			r[i].read();
		}
		int s = b + 1, t = b + 2;
		ec = 0; memset(header, 0, sizeof(header));
		for (int i = 1; i <= b; ++i) {
			for (int j = 1; j <= b; ++j) {
				if (i == j) continue;
				add(i, j, cal(i, j));
			}
		}
		for (int i = 1; i <= b; ++i) {
			add(s, i, r[i].x0 - 1);
			add(i, t, w - r[i].x1);
		}
		printf("Case #%d: %d\n", tt, min(dijkstra(s, t), w));
	}
	return 0;
}

