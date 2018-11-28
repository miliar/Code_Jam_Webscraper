#include <cstdio>

#define ROW true
#define COLUMN false

#define min(a,b) a < b ? a : b
#define max(a,b) a > b ? a : b

static int N, M, garden[100][100], tarjet[100][100];

void get_arguments() {
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%d", &tarjet[i][j]);
			garden[i][j] = 100;
		}
	}
}

int find_max(int pos, bool dir) {
	int ret;
	if (dir) { // row
		ret = tarjet[pos][0];
		for (int i = 1; i < M; ++i) {
			ret = max(ret, tarjet[pos][i]);
		}
	} else { // column
		ret = tarjet[0][pos];
		for (int i = 1; i < N; ++i) {
			ret = max(ret, tarjet[i][pos]);
		}
	}
	return ret;
}

void cut_the_line(int pos, bool dir, int height) {
	if (dir) { // row
		for (int i = 0; i < M; ++i) {
			garden[pos][i] = min(garden[pos][i], height);
		}
	} else { // column
		for (int i = 0; i < N; ++i) {
			garden[i][pos] = min(garden[i][pos], height);
		}
	}
}

bool compare_gardens() {
	bool ret = true;
	for (int i = 0; ret && i < N; ++i) {
		for (int j = 0; ret && j < M; ++j) {
			if (garden[i][j] != tarjet[i][j]) ret = false;
		}
	}
	return ret;
}

bool solve_problem() {
	for (int i = 0; i < N; ++i) {
		cut_the_line(i, ROW, find_max(i, ROW));
	}
	for (int j = 0; j < M; ++j) {
		cut_the_line(j, COLUMN, find_max(j, COLUMN));
	}
	
	return compare_gardens();
}

int main(int argc, char *argv[]) {
	int ncases;
	int garden[100][100];
	scanf("%d", &ncases);
	for (int n = 0; n < ncases; ++n) {
		get_arguments();
		printf("Case #%d: %s\n", n+1, (solve_problem() ? "YES" : "NO"));
	}
	return 0;
}