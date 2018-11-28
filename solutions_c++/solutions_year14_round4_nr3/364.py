#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#define POW2(k) (1<<(k))
#define POW2L(k) (1ULL<<(k))
#define INSIDE(a, b) (POW2(a) & (b))
#define MERGE(a, b) (POW2(a) | (b))
#define LOWBIT(v) ((v)&(-(v)))
#define INF 0x3f3f3f3f
#define EPS 1e-10
using namespace std;

const double PI = acos(-1.0);

typedef pair<int, int> pii;
typedef long long LL;
typedef unsigned long long ULL;

template<class T1, class T2> inline bool ChkMax(T1 &a, const T2 &b) { if (a < b) { a = b; return true; } return false; }
template<class T1, class T2> inline bool ChkMin(T1 &a, const T2 &b) { if (a > b) { a = b; return true; } return false; }

#define MAX_N 1003
#define MAXN 200000
#define MAXE 1000000
#define MOD 1000000007

struct EDGE {
	int v, cap;
	EDGE *next, *rev;
}*edge[MAXN], data[MAXE], *curE[MAXN], *revE[MAXN];
int tot, src, snk, node;

void initG(int _src, int _snk, int _node) {
	tot = 0;
	src = _src; snk = _snk;	node = _node;
	memset(edge, 0, sizeof(edge));
}

void makeE(EDGE *cur, EDGE *rev, int u, int v, int c) {
	cur->v = v;	cur->cap = c;	cur->rev = rev;
	cur->next = edge[u];	edge[u] = cur;
}

void link(int u, int v, int c) {
	makeE(&data[tot], &data[tot + 1], u, v, c);
	makeE(&data[tot + 1], &data[tot], v, u, 0);
	tot += 2;
}

int q[MAXN], dis[MAXN], cnt[MAXN];
void revBfs() {
	memset(dis, 0x3f, sizeof(dis));
	memset(cnt, 0, sizeof(cnt));
	int bgn = 0, rear = 0;
	q[rear++] = snk;	cnt[0] = 1;	dis[snk] = 0;
	while (bgn < rear) {
		int u = q[bgn++];
		for (EDGE *cur = edge[u]; cur; cur = cur->next) {
			if (dis[cur->v] == INF) {
				dis[cur->v] = dis[u] + 1;
				cnt[dis[cur->v]]++;
				q[rear++] = cur->v;
			}
		}
	}
}

int augment() {
	int key = INF;
	for (int u = src; u != snk; u = curE[u]->v) {
		key = min(key, curE[u]->cap);
	}

	for (int u = src; u != snk; u = curE[u]->v) {
		curE[u]->cap -= key;
		curE[u]->rev->cap += key;
	}

	return key;
}

int isap() {
	revBfs();
	memcpy(curE, edge, sizeof(edge));

	int flow = 0, u = src;
	while (dis[src] <= node) {
		if (u == snk) {
			flow += augment();
			u = src;
		}

		EDGE *cur = curE[u];
		for (; cur; cur = cur->next) {
			if (cur->cap && dis[cur->v] + 1 == dis[u])
				break;
		}

		if (cur) {
			curE[u] = cur;
			revE[cur->v] = cur->rev;
			u = cur->v;
		} else {
			if (!(--cnt[dis[u]]))
				break;

			curE[u] = edge[u];
			int d = node;
			for (cur = edge[u]; cur; cur = cur->next) {
				if (cur->cap) {
					d = min(d, dis[cur->v]);
				}
			}
			dis[u] = d + 1;
			++cnt[dis[u]];

			if (u != src)
				u = revE[u]->v;
		}
	}

	return flow;
}

int W, H, B;
struct Data {
	int x0, y0, x1, y1;
} rect[MAX_N];
bool flag[MAX_N][MAX_N];

int getId(int w, int h, int level) {
	return h*W + w + W*H*level;
}

const int dx[] = { 0, 0, 1, -1 };
const int dy[] = { 1, -1, 0, 0 };

int solve() {
	memset(flag, 0, sizeof(flag));
	for (int i = 0; i < B; ++i) {
		for (int x = rect[i].x0; x <= rect[i].x1; ++x) {
			for (int y = rect[i].y0; y <= rect[i].y1; ++y) {
				flag[x][y] = true;
			}
		}
	}
	int src = W*H * 2;
	int snk = src + 1;
	initG(src, snk, W*H * 2 + 2);
	for (int i = 0; i < W; ++i) {
//		if (!flag[i][0]) {
		link(src, getId(i, 0, 0), 1);
//		}
//		if (!flag[i][H - 1]) {
		link(getId(i, H - 1, 1), snk, 1);
//		}
	}
	for (int i = 0; i < W; ++i) {
		for (int j = 0; j < H; ++j) {
			if (!flag[i][j]) {
				link(getId(i, j, 0), getId(i, j, 1), 1);
			}
			for (int d = 0; d < 4; ++d) {
				int w = i + dx[d];
				int h = j + dy[d];
				if (0 <= w && w < W && 0 <= h && h < H) {
//					if (!flag[w][h]) {
					link(getId(i, j, 1), getId(w, h, 0), 1);
//					}
				}
			}
		}
	}
	return isap();
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt1.in", "r", stdin);
//	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		scanf("%d %d %d", &W, &H, &B);
		for (int i = 0; i < B; ++i) {
			scanf("%d %d %d %d", &rect[i].x0, &rect[i].y0, &rect[i].x1, &rect[i].y1);
		}
		printf("Case #%d: %d\n", cas, solve());
	}

	return 0;
}
