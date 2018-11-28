#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

const int MAX_N = 100 + 10;
int n, m;
int a[MAX_N][MAX_N];
int row[MAX_N], col[MAX_N];

void work() {
	cin >> n >> m;
	fill(row, row + n, 0);
	fill(col, col + m, 0);
	for (int r = 0; r < n; ++r) {
		for (int c = 0; c < m; ++c) {
			scanf("%d", a[r] + c);
			row[r] = max(row[r], a[r][c]);
			col[c] = max(col[c], a[r][c]);
		}
	}

	for (int r = 0; r < n; ++r) {
		for (int c = 0; c < m; ++c) {
			if (a[r][c] != min(row[r], col[c])) {
				puts("NO");
				return;
			}
		}
	}
	puts("YES");
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
