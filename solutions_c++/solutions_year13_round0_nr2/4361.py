#include <cstdio>
#include <algorithm>
using namespace std;

int grid[105][105];
int rowmax[105];
int colmax[105];

int main() {
	int ncases;
	scanf("%d", &ncases);
	for (int tcase = 1; tcase <= ncases; tcase++) {
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			rowmax[i] = -1;
		}
		for (int j = 0; j < m; j++) {
			colmax[j] = -1;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &grid[i][j]);
				rowmax[i] = max(grid[i][j], rowmax[i]);
				colmax[j] = max(grid[i][j], colmax[j]);
			}
		}
		bool okay = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!(grid[i][j] >= rowmax[i] || grid[i][j] >= colmax[j])) {
					okay = false;
					break;
				}
			}
			if (!okay) {
				break;
			}
		}
		if (okay) {
			printf("Case #%d: YES\n", tcase);
		} else {
			printf("Case #%d: NO\n", tcase);
		}
	}
}
