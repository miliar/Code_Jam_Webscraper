#include <cstdio>
#include <algorithm>
#define MAXN 100

bool solve(int N, int M, int lawn[MAXN][MAXN])
{
	int maxh_row[N];
	int maxh_col[M];

	for(int i = 0; i < N; ++i) {
		maxh_row[i] = 0;
		for(int j = 0; j < M; ++j) {
			maxh_row[i] = std::max(maxh_row[i], lawn[i][j]);
		}
	}

	for(int i = 0; i < M; ++i) {
		maxh_col[i] = 0;
		for(int j = 0; j < N; ++j) {
			maxh_col[i] = std::max(maxh_col[i], lawn[j][i]);
		}
	}

	for(int i = 0; i < N; ++i) {
		for(int j = 0; j < M; ++j) {
			if((lawn[i][j] < maxh_row[i]) && (lawn[i][j] < maxh_col[j])) {
				return false;
			}
		}
	}

	return true;
}

int main(int argc, char **argv)
{
	int T;

	int N, M;
	int lawn[MAXN][MAXN];

	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		scanf("%d%d", &N, &M);
		for(int j = 0; j < N; ++j) {
			for(int k = 0; k < M; ++k) {
				scanf("%d", &lawn[j][k]);
			}
		}

		bool possible = solve(N, M, lawn);
		printf("Case #%d: %s\n", i, possible ? "YES" : "NO");
	}

	return 0;
}
