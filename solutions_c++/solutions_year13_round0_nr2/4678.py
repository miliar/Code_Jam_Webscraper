#include <cstdio>
#include <algorithm>

using namespace std;

int n, m;
int table[200][200];
int row[200], col[200];

int solve() {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (min(row[i], col[j]) != table[i][j]) {
				return 0;
			}
		}
	}
	return 1;
}

int main() {
	int r;
	scanf("%d", &r);
	for (int cs = 1; cs <= r; ++cs) {
		printf("Case #%d: ", cs);
		scanf("%d %d", &n, &m);
		fill(row, row + 200, 0);
		fill(col, col + 200, 0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &table[i][j]);
				row[i] = max(row[i], table[i][j]);
				col[j] = max(col[j], table[i][j]);
			}
		}

		printf("%s\n", solve() ? "YES" : "NO");
	}
	return 0;
}
