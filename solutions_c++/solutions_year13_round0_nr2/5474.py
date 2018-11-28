#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int T, m, n, a[105][105], mr[105], mc[105];

bool solve() {
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < n; ++j) {
			if (a[i][j] < mr[i] && a[i][j] < mc[j]) return false;
		}
	}
	return true;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &m, &n);
		memset(mr, 0, sizeof(mr));
		memset(mc, 0, sizeof(mc));
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				scanf("%d", &a[i][j]);
				mr[i] = max(mr[i], a[i][j]);
				mc[j] = max(mc[j], a[i][j]);
			}
		}
		if (solve()) printf("Case #%d: YES\n", tc);
		else printf("Case #%d: NO\n", tc);
	}
	return 0;
}
