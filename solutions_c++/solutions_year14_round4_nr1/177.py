#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int v[705];

void work() {
	int n, m; memset(v, 0, sizeof(v));
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i) {
		int x; scanf("%d", &x); v[x]++;
	}

	int ans = 0;
	for (int k = m; k >= 0; --k) {
		while (v[k] > 0) {
			ans++; v[k]--;

			for (int i = m - k; i >= 0; --i) if (v[i] > 0) {
				v[i]--; break;
			}

		}
	}

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
