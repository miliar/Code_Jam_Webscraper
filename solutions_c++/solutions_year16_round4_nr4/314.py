#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define Clear(a, b) memset(a, b, sizeof a)
#define fi first
#define se second

typedef long long i64;
typedef pair<int, int> Data;

const int N = 30;

int n, m, a[N][N];
Data b[N * N];
bool peo[N], mac[N], sol;

void Dfs(int x) {
	for (int i = 1; i <= n; ++i)
		if (!peo[i]) {
			peo[i] = 1;
			bool have = 0;
			for (int j = 1; j <= n; ++j)
				if (a[i][j] && !mac[j])
					have = 1;
			if (!have) {
				sol = 0;
				return;
			}
			for (int j = 1; j <= n; ++j) {
				if (a[i][j] && !mac[j]) {
					mac[j] = 1;
					Dfs(x + 1);
					mac[j] = 0;
				}
			}
			peo[i] = 0;
		}
}

int main() {
	freopen("data.in", "r", stdin);

	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		printf("Case #%d: ", t);
		scanf("%d", &n);
		m = 0;
		for (int i = 1; i <= n; ++i) 
			for (int j = 1; j <= n; ++j) {
				char c;
				scanf(" %c", &c);
				a[i][j] = c - '0';
				if (!a[i][j])
					b[++m] = Data(i, j);
			}
		int full = (1 << m) - 1;
		int ans = m;
		for (int i = 0; i <= full; ++i) {
			int s = 0;
			for (int j = 1; j <= m; ++j)
				if ((i >> (j - 1)) & 1) {
					int x = b[j].fi, y = b[j].se;
					a[x][y] = 1;
					++s;
				}
			Clear(peo, 0);
			Clear(mac, 0);
			sol = 1;
			Dfs(1);
			if (sol) 
				ans = min(ans, s);
			for (int j = 1; j <= m; ++j)
				if ((i >> (j - 1)) & 1) {
					int x = b[j].fi, y = b[j].se;
					a[x][y] = 0;
				}
		}
		printf("%d\n", ans);
	}

	return 0;
}
