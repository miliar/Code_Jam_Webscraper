#include <cstdio>
#include <cstring>

int board[60][60];
int q[60];

const char *str = ".*c";

int check_cr(int i, int j, int r, int c) {
	return i >= 0 && i < r && j >= 0 && j < c;
}

int check(int i, int j, int r, int c) {
	if (board[i][j]) return 0;
	int res = 1;
	board[i][j] = 2;
	int mine = 0;
	for (int dr = -1; dr <= 1; dr++) {
		for (int dc = -1; dc <= 1; dc++) {
			if (check_cr(i + dr, j + dc, r, c)) {
				mine += board[i + dr][j + dc] == 1;
			}
		}
	}
	if (!mine) {
		for (int dr = -1; dr <= 1; dr++) {
			for (int dc = -1; dc <= 1; dc++) {
				if (check_cr(i + dr, j + dc, r, c)) {
					res += check(i + dr, j + dc, r, c);
				}
			}
		}
	}
	return res;
}

void solve(int test) {
	int r, c; scanf("%d%d", &r, &c);
	int m; scanf("%d", &m);
	printf("Case #%d:\n", test);
	int nn = r * c;
	for (int mask = 0; mask < (1 << nn); mask++) {
		if (__builtin_popcount(mask) != m) continue;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				for (int ii = 0; ii < r; ii++) {
					for (int jj = 0; jj < c; jj++) {
						board[ii][jj] = (mask >> (ii * c + jj)) & 1;
					}
				}
				if (check(i, j, r, c) == r * c - m) {
					for (int ii = 0; ii < r; ii++) {
						for (int jj = 0; jj < c; jj++) {
							if (ii == i && j == jj) {
								printf("c");
							} else if (board[ii][jj] == 1) {
								printf("*");
							} else {
								printf(".");
							}
						}
						printf("\n");
					}
					return;
				}
			}
		}
	}
	printf("Impossible\n");
}

int main() {
	int T; scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}
}
