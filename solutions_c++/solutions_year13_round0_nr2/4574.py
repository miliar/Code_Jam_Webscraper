#include <cstdio>

const int MAX = 104;

int r, c;
int grid[MAX][MAX];

int m(int a, int b) { return a > b ? a : b; }

bool proc() {
	scanf("%d %d", &r, &c);

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			scanf("%d ", &grid[i][j]);
		}
	}

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			bool okay = false;
			int max = 0;
			for (int k = 0; k < r; k++) {
				max = m(max, grid[k][j]);
			}
			if (max == grid[i][j]) {
				okay = true;
			}
			max = 0;
			for (int k = 0; k < c; k++) {
				max = m(max, grid[i][k]);
			}
			if (max == grid[i][j]) {
				okay = true;
			}
			if (!okay) {
				return false;
			}
		}
	}

	return true;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		if (proc()) {
			printf("YES");
		} else {
			printf("NO");
		}
		printf("\n");
	}
	return 0;
}
