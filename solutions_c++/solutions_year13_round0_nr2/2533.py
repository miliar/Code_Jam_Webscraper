#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int lawn[101][101];
int max_row[101], max_col[101];
int main() {
	int T;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf_s("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, m;

		memset(max_row, 0, sizeof(max_row));
		memset(max_col, 0, sizeof(max_col));

		scanf_s("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf_s("%d", lawn[i] + j);
			}
		}

		bool yes = true;
		// horizontal
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				max_row[i] = max(max_row[i], lawn[i][j]);
			}
		}
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				max_col[i] = max(max_col[i], lawn[j][i]);
			}
		}

		for (int i = 0; i < n && yes; i++) {
			for (int j = 0; j < m; j++) {
				if (max_row[i] != lawn[i][j] && max_col[j] != lawn[i][j]) {
					yes = false;
					break;
				}
			}
		}

		printf("Case #%d: %s\n", t, yes ? "YES" : "NO");
	}
	return 0;
}