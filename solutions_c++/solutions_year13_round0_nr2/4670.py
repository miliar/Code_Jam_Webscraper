#include <cstdio>
#include <cstring>

const int MAXN = 100 + 10;
int a[MAXN][MAXN], b[MAXN][MAXN], c[MAXN][MAXN], bb[MAXN], cc[MAXN];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int task, TT = 0;
	scanf("%d", &task);
	while (task --) {
		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		int ans = true;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				int b1 = false, b2 = false;
				for (int k = 0; k < n; k++) if (a[k][j] > a[i][j]) b1 = true;
				for (int k = 0; k < m; k++) if (a[i][k] > a[i][j]) b2 = true;
				if (b1 && b2) ans = false;
			}
		if (ans) printf("Case #%d: YES\n", ++TT);
		else printf("Case #%d: NO\n", ++TT);
	}
	return 0;
}
