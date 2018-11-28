#include <cstdio>

using namespace std;

int main() {
	int map[100][100];
	int mps[100][100];
	int k;
	scanf("%d", &k);
	for (int t = 1; t <= k; ++t) {
		printf("Case #%d: ", t);
		
		int n,m;
		scanf("%d %d", &n, &m);
		
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &map[i][j]);
				mps[i][j] = 100;
			}
		}
		
		bool calc = true;
		while (calc) {
			calc = false;
			for (int i = 0; i < n; ++i) {
				int t = map[i][0];
				for (int j = 1; j < m; ++j) if (map[i][j] > t) t = map[i][j];
				for (int j = 0; j < m; ++j) {
					if (mps[i][j] > t) {calc = true;
						mps[i][j] = t;
					}
				}
			}
			for (int j = 0; j < m; ++j) {
				int t = map[0][j];
				for (int i = 1; i < n; ++i) if (map[i][j] > t) t = map[i][j];
				for (int i = 0; i < n; ++i) {
					if (mps[i][j] > t) {calc = true;
						mps[i][j] = t;
					}
				}
			}
		}
		
		bool ok = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (map[i][j] != mps[i][j]) ok = false;
			}
		}
		if (ok) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}
