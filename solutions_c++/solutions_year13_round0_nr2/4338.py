#include <cstdio>
#include <algorithm>

int ht[102][102];
int nht[102][102];
int m, n;

bool all_row(int r, int h) {
	for (int i = 0; i < m; i++) {
		if (ht[r][i] != h) return false;
	}
	return true;
}

bool all_col(int c, int h) {
	for (int i = 0; i < n; i++) {
		if (ht[i][c] != h) return false;
	}
	return true;
}

bool solve() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &nht[i][j]);
		}
	}

	for (int h = 1; h <= 100; h++) {
		// copy over
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				ht[i][j] = nht[i][j];
			}
		}

		// uncut rows
		for (int i = 0; i < n; i++) {
			if (all_row(i, h)) {
				// uncut
				for (int j = 0; j < m; j++) nht[i][j]++;
			}
		}

		// uncut cols
		for (int i = 0; i < m; i++) {
			if (all_col(i, h)) {
				for (int j = 0; j < n; j++) nht[j][i]++;
			}
		}

		// verify that every height is > h
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (nht[i][j] <= h) return false;
	}

	return true;
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		if (solve()) printf("YES\n");
		else printf("NO\n");
	}
}