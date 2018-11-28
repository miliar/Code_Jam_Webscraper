#include <bits/stdc++.h>
using namespace std;

const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1, 0};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1, 0};

const int S = 55;

int n, m, k;
bool a[S][S], b[S][S], was[S][S], used[S][S], p[S*S], was2[S][S];

int f(int n, int m) {
	if (n == 1) return m;
	if (m == 1) return n;
	return n+n+m+m-4;
}

void dfs(int x, int y) {
	was[x][y] = 1;
	for (int k = 0; k < 8; k++) {
		int i = x + dx[k];
		int j = y + dy[k];
		if (1 <= i && i <= n && 1 <= j && j <= m && a[i][j] == 0 && !was[i][j])
			dfs(i, j);
	}
}

void dfs2(int x, int y) {
	was2[x][y] = 1;
	for (int k = 0; k < 8; k++) {
		int i = x + dx[k];
		int j = y + dy[k];
		if (1 <= i && i <= n && 1 <= j && j <= m && b[i][j] == 1 && !was2[i][j])
			dfs2(i, j);
	}
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%d %d %d", &n, &m, &k);
		
		if (k+1 == n*m) {
			printf("Case #%d:\n", t);
			for (int r = 1; r <= n; r++) {
				for (int c = 1; c <= m; c++) {
					if (r == 1 && c == 1) {
						putchar('c');
					} else
						putchar('*');
				}
				printf("\n");
			}
			continue;
		}

		int N = n*m;

		memset(p, 0, sizeof p);
		for (int i = 1; i <= k; i++)
			p[N-i] = 1;

		bool exist = 0;

		do {
			int cc = 0;
			for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				a[i][j] = p[cc++];

			int cnt = 0; // components
			memset(was, 0, sizeof was);

			for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				if (a[i][j] == 0 && !was[i][j]) {
					dfs(i, j);
					cnt++; if (cnt != 1) break;
				}
			}
			if (cnt != 1) continue;

			int num = 0;
			memset(used, 0, sizeof used);

			for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				bool ok = 1;
				for (int k = 8; ok && k >= 0; k--) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (1 <= x && x <= n && 1 <= y && y <= m && a[x][y] == 1)
						ok = 0;
				}

				b[i][j] = ok;
				if (!ok) continue;

				for (int k = 0; k < 9; k++) {
					int x = i + dx[k];
					int y = j + dy[k];
					if (1 <= x && x <= n && 1 <= y && y <= m && !used[x][y]) {
						used[x][y] = 1;
						num++;
					}
				}
			}

			if (num != n*m-k) continue;

/*			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= m; j++)
					cout << a[i][j];
				cout << endl;
			}
			cout << endl;

			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= m; j++)
					cout << b[i][j];
				cout << endl;
			}
			cout << endl;
			cout << endl;*/

			int sx, sy;

			int cnt2 = 0; // components of 8-free
			memset(was2, 0, sizeof was2);

			for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				if (b[i][j] == 1 && !was2[i][j]) {
					dfs2(i, j);
					sx = i, sy = j;
					cnt2++; if (cnt2 != 1) break;
				}
			}

			if (cnt2 != 1) continue;

			exist = 1;
			printf("Case #%d:\n", t);
			for (int r = 1; r <= n; r++) {
				for (int c = 1; c <= m; c++) {
					if (r == sx && c == sy) {
						putchar('c');
					} else
					if (a[r][c])
						putchar('*');
					else
						putchar('.');
				}
				printf("\n");
			}
			break;
		} while (next_permutation(p, p + N));

		if (!exist)
		printf("Case #%d:\nImpossible\n", t);
	}

	return 0;
}
