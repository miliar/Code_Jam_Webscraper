#include <cstdio>
#include <algorithm>
#include <cstring>

using std::min;
using std::max;

const int N = 111;

int r, c;
char map[N][N];

bool next[N][N];

int count_row[N], count_col[N];

char read_grid(void) {
	char c;
	do {
		scanf("%c", &c);
	} while (c != '.' && c != '<' && c != '>' && c != '^' && c != 'v');
	return c;
}

bool find(int r0, int c0, int dr, int dc) {
	int r1 = r0, c1 = c0;
	while (1) {
		r1 += dr;
		c1 += dc;
		if (r1 == 0 || r1 > r || c1 == 0 || c1 > c) break;
		if (map[r1][c1] != '.') {
			return true;
		}
	}
	return false;
}

int solve() {
	scanf("%d%d", &r, &c);
	for (int i = 1; i <= r; ++ i) {
		for (int j = 1; j <= c; ++ j) {
			map[i][j] = read_grid();
		}
	}
	memset(count_row, 0, sizeof(count_row));
	memset(count_col, 0, sizeof(count_col));
	for (int i = 1; i <= r; ++ i) {
		for (int j = 1; j <= c; ++ j) {
			if (map[i][j] == '<') {
				next[i][j] = find(i, j, 0, -1);
			}
			if (map[i][j] == '>') {
				next[i][j] = find(i, j, 0, +1);
			}
			if (map[i][j] == '^') {
				next[i][j] = find(i, j, -1, 0);
			}
			if (map[i][j] == 'v') {
				next[i][j] = find(i, j, +1, 0);
			}
			if (map[i][j] != '.') {
				count_row[i] += 1;
				count_col[j] += 1;
			}
		}
	}
	int result = 0;
	for (int i = 1; i <= r; ++ i) {
		for (int j = 1; j <= c; ++ j) {
			if (map[i][j] != '.' && !next[i][j]) {
				if (count_row[i] == 1 && count_col[j] == 1) {
					return -1;
				} else {
					++ result;
				}
				//printf("%d %d : %d\n", i, j, result);
			}
		}
	}
	return result;
}

int main(void) {
	int test_count;
	scanf("%d", &test_count);
	for (int test = 1; test <= test_count; ++ test) {
		printf("Case #%d: ", test);
		int result = solve();
		if (result == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", result);
		}
	}
	return 0;
}
