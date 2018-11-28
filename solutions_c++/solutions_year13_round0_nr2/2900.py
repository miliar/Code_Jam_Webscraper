#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>

using namespace std;



struct node{
	int v, x, y;
	node () {}
	node (int v1, int x1, int y1) : v(v1), x(x1), y(y1) {}
	bool operator < (const node &e) const {
		return v < e.v;
	}
}T[10011];

int a[111][111], m, n;

bool chk (int x, int y, int v) {
//	printf ("(%d, %d) = %d\n", x, y, v);
	int i, j;
	for (j = 1; j <= n && a[x][j] <= v; ++j);
	for (i = 1; i <= m && a[i][y] <= v; ++i);
	return (j > n) || (i > m);
}

int cnt;
int main () {
	int i, j, k;
	int Te, ca;

	freopen ("b_large.txt", "w", stdout);
	for (scanf ("%d", &Te), ca = 1; ca <= Te; ++ca) {
		scanf ("%d%d", &m, &n);
		cnt = 0;
		for (i = 1; i <= m; ++i)
			for (j = 1; j <= n; ++j) {
				scanf ("%d", &a[i][j]);
				T[cnt++] = node(a[i][j], i, j);
			}
		sort (T, T + cnt);
		for (i = 0; i < cnt && chk (T[i].x, T[i].y, T[i].v); ++i);
		printf ("Case #%d: %s\n", ca, i >= cnt? "YES" : "NO");
	}
	return 0;
}
