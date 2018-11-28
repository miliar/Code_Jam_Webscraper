#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 128;

int a[MAXN][MAXN];
int mr[MAXN], mc[MAXN];

int main() {
	int t;
	scanf("%d", &t);

	for (int ti = 1; ti <= t; ti++) {
		memset(mr, 0, sizeof(mr));
                memset(mc, 0, sizeof(mc));

		int n, m;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);
				mr[i] = max(mr[i], a[i][j]);
				mc[j] = max(mc[j], a[i][j]);
			}
		}

		bool result = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] < mr[i] && a[i][j] < mc[j]) {
					result = false;
				}
			}
		}

		printf("Case #%d: %s\n", ti, result ? "YES" : "NO");
	}
	return 0;
}

