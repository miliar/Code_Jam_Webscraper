#include <cstdio>

int grid[100][100], need[100][100], can[100][100];

int main() {
	FILE * fin = fopen("A.in", "r"), * fout = fopen("A.out", "w");
	int t, T, R, C, i, j, first, last, count;
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d%d", &R, &C);
		for (i = 0; i < R; ++i) {
			getc(fin);
			for (j = 0; j < C; ++j) {
				grid[i][j] = getc(fin);
				need[i][j] = 0;
				can[i][j] = 0;
			}
		}
		for (i = 0; i < R; ++i) {
			first = -1;
			last = -1;
			for (j = 0; j < C; ++j) {
				if (grid[i][j] != '.') {
					first = j;
					break;
				}
			}
			for (++j; j < C; ++j) {
				if (grid[i][j] != '.') {
					last = j;
				}
			}
			if (last != -1) {
				if (grid[i][first] == '<') {
					need[i][first] = 1;
				}
				if (grid[i][last] == '>') {
					need[i][last] = 1;
				}
				for (j = first; j <= last; ++j) {
					can[i][j] = 1;
				}
			} else if (first != -1) {
				if (grid[i][first] == '<' || grid[i][first] == '>') {
					need[i][first] = 1;
				}
			}
		}
		for (i = 0; i < C; ++i) {
			first = -1;
			last = -1;
			for (j = 0; j < R; ++j) {
				if (grid[j][i] != '.') {
					first = j;
					break;
				}
			}
			for (++j; j < R; ++j) {
				if (grid[j][i] != '.') {
					last = j;
				}
			}
			if (last != -1) {
				if (grid[first][i] == '^') {
					need[first][i] = 1;
				}
				if (grid[last][i] == 'v') {
					need[last][i] = 1;
				}
				for (j = first; j <= last; ++j) {
					can[j][i] = 1;
				}
			} else if (first != -1) {
				if (grid[first][i] == '^' || grid[first][i] == 'v') {
					need[first][i] = 1;
				}
			}
		}
		count = 0;
		for (i = 0; i < R; ++i) {
			for (j = 0; j < C; ++j) {
				if (need[i][j]) {
					if (can[i][j]) {
						++count;
					} else {
						break;
					}
				}
			}
			if (j < C) {
				break;
			}
		}
		if (i < R) {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", t);
		} else {
			fprintf(fout, "Case #%d: %d\n", t, count);
		}
	}
	return 0;
}

