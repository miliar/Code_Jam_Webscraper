#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i,a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)

const int maxn = 1000 + 2;

int d[maxn + 2], dist[maxn + 2][maxn + 2];
bool mark[maxn + 2];

int calc(int l, int r, int a, int b)
{
	if (max(l, a) <= min(r, b)) {
		return 0;
	}
	return min(abs(r - a) - 1, abs(l - b) - 1);
}

int xl[maxn], xr[maxn], yl[maxn], yr[maxn];

int solve()
{
	int w, h, b;
	scanf("%d%d%d", &w, &h, &b);
	memset(mark, true, sizeof(mark));
	for (int i = 0; i < b; ++ i) {
		scanf("%d%d%d%d", &xl[i], &yl[i], &xr[i], &yr[i]);
	}
	
	int source = b;
	int sink = b + 1;
	dist[source][sink] = w;
	for (int i = 0; i < b; ++ i) {
		dist[source][i] = xl[i];
		dist[i][sink] = w - 1 - xr[i];
		
		for (int j = 0; j < i; ++ j) {
			int dx = calc(xl[i], xr[i], xl[j], xr[j]);
			int dy = calc(yl[i], yr[i], yl[j], yr[j]);
			dist[i][j] = dist[j][i] = max(dx, dy);
		}
	}
	
	memset(d, -1, sizeof(d));
	memset(mark, false, sizeof(mark));
	d[source] = 0;
	for (int i = 0; i <= sink && !mark[sink]; ++ i) {
		int u = -1;
		for (int j = 0; j <= sink; ++ j) {
			if (d[j] != -1 && !mark[j]) {
				if (u == -1 || d[j] < d[u]) {
					u = j;
				}
			}
		}
		assert(u != -1);
		mark[u] = true;
		for (int v = 0; v <= sink; ++ v) {
			if (d[v] == -1 || d[v] > d[u] + dist[u][v]) {
				d[v] = d[u] + dist[u][v];
			}
		}
	}
	return d[sink];
}

int main()
{
	int tests, test = 1;
	for (scanf("%d", &tests); test <= tests; ++ test) {
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
