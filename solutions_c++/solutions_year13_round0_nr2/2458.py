#include <stdio.h>

int T, M, N;
int lawn[101][101];
int row_max[101], col_max[101];

int main()
{
	int r, c, t;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d", &N, &M);
		for (r = 0; r < N; r++)
			for (c = 0; c < M; c++)
				scanf("%d", &lawn[r][c]);
		for (r = 0; r < N; r++) {
			row_max[r] = lawn[r][0];
			for (c = 1; c < M; c++)
				if (lawn[r][c] > row_max[r])
					row_max[r] = lawn[r][c];
		}
		for (c = 0; c < M; c++) {
			col_max[c] = lawn[0][c];
			for (r = 0; r < N; r++)
				if (lawn[r][c] > col_max[c])
					col_max[c] = lawn[r][c];
		}

		for (r = 0; r < N; r++) {
			for (c = 0; c < M; c++) 
				if (lawn[r][c] < row_max[r] && lawn[r][c] < col_max[c]) break;
			if (c < M) break;
		}
		if (r < N) printf("Case #%d: NO\n", t);
		else printf("Case #%d: YES\n", t);
	}
	return 0;
}

