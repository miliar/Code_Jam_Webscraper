#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std ;
struct Tedge{
    int p ;
    int c ;
    int f ;
    int next ;
} edge[2100000] ;
int n, m, s, t, len, a[210000], map[1100][1100], map2[1100][1100], d[210000], q[210000], last[210000];
void addedge(int s, int t) ;
void init() ;
bool bfs() ;
void solve() ;
int main() {
	freopen("C.in", "r", stdin); freopen("C.out","w",stdout);
	int Test ; cin >> Test ;
	for (int i = 1; i <= Test; i++ ) {
		init() ; printf("Case #%d: ", i) ; solve();
	}
}
void addedge(int s, int t) {
	edge[++len].p = t, edge[len].next = a[s], edge[len].f = len + 1, edge[len].c = 1, a[s] = len;
	edge[++len].p = s, edge[len].next = a[t], edge[len].f = len - 1, edge[len].c = 0, a[t] = len;
}
void init() {
	int k = 0, x1, x2, y1, y2; scanf("%d %d %d", &n, &m, &k); memset(map, 0, sizeof(map));
	while (k--) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int i = x1; i <= x2; ++i) for (int j = y1; j <= y2; ++j) map[i][j] = -1;
	}
	s = 0; memset(a, 0xff, sizeof(a)); len = 0;
	for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (map[i][j] == 0) {
		map[i][j] = (++s); map2[i][j] = (++s);
		addedge(map[i][j], map2[i][j]);
	}
	++s; t = s + 1;
	for (int i = 0; i < n; ++i) {
		if (map[i][0] >= 0) addedge(s, map[i][0]);
		if (map[i][m - 1] >= 0) addedge(map2[i][m - 1], t);
	}
	for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (map[i][j] >= 0) {
		if (i + 1 < n && map[i + 1][j] >= 0) addedge(map2[i][j], map[i + 1][j]), addedge(map2[i + 1][j], map[i][j]);
        if (j + 1 < m && map[i][j + 1] >= 0) addedge(map2[i][j], map[i][j + 1]), addedge(map2[i][j + 1], map[i][j]);
	}
}
bool bfs() {
	memset(d, 0xff, sizeof(d)); int st = 0, ed = 1, i, k; q[1] = s; d[s] = 0;
	while (st < ed) {
        k = q[++st];
		for (i = a[k]; i != -1; i = edge[i].next) if (edge[i].c > 0 && d[edge[i].p] < 0){
			d[edge[i].p] = d[k] + 1, q[++ed] = edge[i].p, last[edge[i].p] = i;
			if (edge[i].p == t) return true;
		}
	}
	return false;
}
void solve() {
	int ans = 0;
	while (bfs()) {
		++ans;
		for (int cur = t; cur != s; cur = edge[edge[last[cur]].f].p)
			--edge[last[cur]].c, ++edge[edge[last[cur]].f].c;
	}
	printf("%d\n", ans);
}
