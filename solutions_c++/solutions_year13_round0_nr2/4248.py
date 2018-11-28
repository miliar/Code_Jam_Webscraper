#include <cstdio>

using namespace std;

const int MAXN = 110;

int rmax[MAXN];
int cmax[MAXN];
int grid[MAXN][MAXN];

int Q;
int N, M;

int main() {
	scanf("%d", &Q);
	for(int q = 1; q <= Q; ++q) {
		printf("Case #%d: ", q);
		scanf("%d %d", &N, &M);

		for(int i = 0; i < MAXN; ++i) rmax[i] = cmax[i] = 0;

		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < M; ++j) {
				scanf("%d", grid[i] + j);
				if (grid[i][j] > rmax[i]) rmax[i] = grid[i][j];
				if (grid[i][j] > cmax[j]) cmax[j] = grid[i][j];
			}
		}

		bool ans = true;
		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < M; ++j) {
				if (grid[i][j] != rmax[i] && grid[i][j] != cmax[j]) {
					ans = false;
				}
			}
		}

		if (ans) printf("YES\n");
		else printf("NO\n");
	}

	return 0;
}
