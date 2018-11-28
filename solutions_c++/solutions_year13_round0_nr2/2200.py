#include <cstdio>
#include <algorithm>

const int MAX_NM = 105;
int T, N, M, board[MAX_NM][MAX_NM], maxesc[MAX_NM], maxesr[MAX_NM];

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d", &N, &M);
		for (int i = 0; i < MAX_NM; ++i) {
			maxesc[i] = maxesr[i] = -1;
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				scanf("%d", &board[i][j]);
				maxesc[j] = std::max(board[i][j], maxesc[j]);
				maxesr[i] = std::max(board[i][j], maxesr[i]);
			}
		}

		bool possible = true;
		for (int c = 0; c < M; ++c) {
			for (int r = 0; r < N; ++r) {
				if (board[r][c] == maxesc[c]) {
					continue;
				}
				if (board[r][c] < maxesr[r]) {
					possible = false;
				}
			}
		}
		printf("Case #%d: %s\n", t, possible ? "YES" : "NO");
	}
}
