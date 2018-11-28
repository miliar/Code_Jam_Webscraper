#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 1010;

struct Edge {
	int y; Edge *next;
}*a[MAXN];

struct Rect {
	int x1, y1, x2, y2;
}c[MAXN];

int Get(Rect a, Rect b) {
	if (!(a.x1 > b.x2 || a.x2 < b.x1)) {
		return min(abs(a.y1 - b.y2), abs(a.y2 - b.y1)) - 1;
	}
	if (!(a.y1 > b.y2 || a.y2 < b.y1)) {
		return min(abs(a.x1 - b.x2), abs(a.x2 - b.x1)) - 1;
	}
	if (a.x1 < b.x1) swap(a, b);
	if (a.y1 > b.y2) {
		return max(abs(a.x1 - b.x2), abs(a.y1 - b.y2)) - 1;
	} else {
		return max(abs(a.x1 - b.x2), abs(a.y2 - b.y1)) - 1;
	}
}

int vs, vt, dis[MAXN][MAXN];
int d[MAXN], vis[MAXN];

int main(void) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		memset(dis, 0x3f, sizeof dis);
		int n, m, k; scanf("%d%d%d", &n, &m, &k); vs = k + 1, vt = k + 2;
		for (int i = 1; i <= k; i++) 
			scanf("%d%d%d%d", &c[i].x1, &c[i].y1, &c[i].x2, &c[i].y2);
		for (int i = 1; i <= k; i++) {
			dis[i][i] = 0;
			for (int j = i + 1; j <= k; j++) {
				dis[j][i] = dis[i][j] = Get(c[i], c[j]);
			}
			dis[vs][i] = dis[i][vs] = c[i].x1;
			dis[vt][i] = dis[i][vt] = n - c[i].x2 - 1;
		}
		dis[vs][vt] = dis[vt][vs] = n;
		memset(d, 0x3f, sizeof d); memset(vis, 0, sizeof vis);
		d[vs] = 0;
		for (int i = 2; i <= k + 2; i++) {
			int w = 0;
			for (int j = 1; j <= k + 2; j++) if (!vis[j] && d[j] < d[w]) w = j;
			vis[w] = 1;
			for (int j = 1; j <= k + 2; j++) if (!vis[j] && d[j] > d[w] + dis[w][j]) {
				d[j] = d[w] + dis[w][j];
			}
		}
		printf("Case #%d: %d\n", _, d[vt]);
	}
	return 0;
}

