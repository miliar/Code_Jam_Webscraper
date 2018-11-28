#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 5)
using namespace std;

int a[MAXN][MAXN];
int used[MAXN][MAXN];
int n, m, k;
int cnt[1 << 21];

int row[MAXN], col[MAXN];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void dfs(int r, int c) {
	used[r][c] = 1;

	for (int i=0; i < 4; ++i) {
		int nr = r + dx[i], nc = c + dy[i];
		if (nr < 0 || nr >= n) continue;
		if (nc < 0 || nc >= m) continue;
		if (used[nr][nc]) continue;
		if (a[nr][nc]) continue;

		dfs(nr, nc);
	}
}

inline void read() {
	cin >> n >> m >> k;
}

inline void solve() {
	int N = n*m;

	for (int i=0; i < n; ++i)
		for (int j=0; j < m; ++j)
			row[i*m + j] = i,
			col[i*m + j] = j;

	int ans = N;
	for (int mask=0; mask < (1 << N); ++mask) {
		int am = cnt[mask];
		if (am >= ans) continue;

		for (int i=0; i < N; ++i) {
			a[ row[i] ][ col[i] ] = ((mask & (1 << i)) > 0);
			used[ row[i] ][ col[i] ] = 0;
		}

		for (int i=0; i < N; ++i) {
			int r = row[i], c = col[i];
			if (r > 0 && c > 0 && (r < n-1) && (c < m-1)) continue;
			if (a[r][c]) continue;
			if (used[r][c]) continue;

			dfs(r, c);
		}

		int br = 0;
		for (int i=0; i < N; ++i)
			br += used[ row[i] ][ col[i] ];

		if (N-br >= k) ans = am;
	}

	cout << ans << endl;
}

inline void pre() {
	for (int i=0; i < (1 << 20); ++i)
		cnt[i] = __builtin_popcount(i);
}

int main() {
	int brt;
	scanf("%d", &brt);
	pre();
	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}