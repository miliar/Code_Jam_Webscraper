#include <stdio.h>
#include <string.h>
#define N 102

int mat[N][N];
int maR[N], maC[N];

int max(int a, int b) {
	return a > b ? a : b;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int index = 1; index <= T; index++) {
		int n, m; scanf("%d %d", &n, &m);
		int i, j;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
				scanf ("%d", &mat[i][j]);
		memset(maR, 0, sizeof maR);
		memset(maC, 0, sizeof maC);
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++) {
				maR[i] = max(maR[i], mat[i][j]);
				maC[j] = max(maC[j], mat[i][j]);
			}
		bool f = true;
		for (i = 0; i < n && f; i++)
			for (j = 0; j < m && f; j++)
				if (mat[i][j] < maR[i] && mat[i][j] < maC[j])
					f = false;
		if (f)
			printf("Case #%d: YES\n", index);
		else 
			printf("Case #%d: NO\n", index);
	}
	return 0;
}