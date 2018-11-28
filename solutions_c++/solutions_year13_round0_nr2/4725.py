#include <cstdio>

int main() {
	int T, N, M, a[102][102], i, j, k;
	bool p;

	freopen("lawn.in", "r", stdin);
	freopen("lawn.out", "w", stdout);

	scanf("%d\n", &T);
	for (k = 0; k < T; ++k) {
		for (i = 0; i < 102; ++i)
			a[0][i] = a[i][0] = 0;
		scanf("%d %d\n", &N, &M);
		for (i = 1; i <= N; ++i)
			for (j = 1; j <= M; ++j) {
				scanf("%d", &a[i][j]);
				if (a[i][j] > a[i][0])
					a[i][0] = a[i][j];
				if (a[i][j] > a[0][j])
					a[0][j] = a[i][j];
			}
		p = true;
		for (i = 1; i <= N; ++i)
			for (j = 1; j <= M; ++j)
				if ((a[i][j] != a[i][0]) and (a[i][j] != a[0][j]))
					p = false;
		if (p)
			printf("Case #%d: YES\n", k + 1);
		else
			printf("Case #%d: NO\n", k + 1);
	}
	

	fclose(stdin);
	fclose(stdout);

	return 0;
}
