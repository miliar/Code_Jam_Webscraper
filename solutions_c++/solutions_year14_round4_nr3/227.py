#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>
#include <numeric>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, 1, -1, 0};
const int MAXN = 400000;
const int MAXE = 800000;

int w, h, n, was[MAXN], bad[105][505], step = 1, edges;
int x1[1005], x2[1005], y1[1005], y2[1005], sink, sor;

int first[MAXN], next[MAXE], end[MAXE], cap[MAXE];

void load() {
	scanf ("%d%d%d", &w, &h, &n);

	for (int i = 0;i < n;i++) {
		scanf ("%d%d%d%d", &x1[i], &y1[i], &x2[i], &y2[i]);
	}
}

void addEdge (int v, int u, int c) {
	next[edges] = first[v];
	end[edges] = u;
	cap[edges] = c;
	first[v] = edges++;
}

bool go (int v, int &amin) {
	if (v == sink) return true;
	was[v] = step;

	for (int i = first[v];i != -1;i = next[i]) {
		int u = end[i];
		if (cap[i] == 0 || was[u] == step) continue;

		int cmin = min (amin, cap[i]);
		if (go (u, cmin)) {
			amin = cmin;
			cap[i] -= cmin;
			cap[i ^ 1] += cmin;
			return true;
		}
	}
	return false;
}

bool good (int x, int y) {
	return x >= 0 && x < w && y >= 0 && y < h;
}

void solve(int test) {
	memset (bad, 0, sizeof (was));
	for (int i = 0;i < n;i++) {
		for (int x = x1[i];x <= x2[i];x++) {
			for (int y = y1[i];y <= y2[i];y++) {
				bad[x][y] = 1;
			}
		}
	}
	sor = 2 * w * h + 5;
	sink = sor + 1;
	memset (first, -1, sizeof (first));
	edges = 0;
	for (int i = 0;i < w;i++) {
		for (int j = 0;j < h;j++) {
			if (bad[i][j]) continue;
			int l = i * h + j;
			int r = i * h + j + w * h;

			for (int k = 0;k < 2;k++) {
				int nx = i + dx[k];
				int ny = j + dy[k];
				if (good (nx, ny) && !bad[nx][ny]) {
					addEdge (r, nx * h + ny, 1);
					addEdge (nx * h + ny, r, 0);
					addEdge (nx * h + ny + w * h, l, 1);
					addEdge (l, nx * h + ny + w * h, 0);
				}	
			}
			if (j == 0) {
				addEdge (sor, l, 1);
				addEdge (l, sor, 0);
			}
			if (j == h - 1) {
				addEdge (r, sink, 1);
				addEdge (sink, r, 0);
			}
			addEdge (l, r, 1);
			addEdge (r, l, 0);
		}
	}

	int ans = 0;
	for (int flow = 100;go (sor, flow);step++) {
		ans += flow;
	}

	printf ("Case #%d: %d\n", test, ans);
}

int main() {
 	freopen ("a.in", "r", stdin);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		load();
 		solve(i);
 	}

 	return 0;
}