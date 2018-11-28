#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

void work() {
	int a, n; scanf("%d%d", &a, &n);
	vector<int> f; f.clear();
	for (int i = 0; i < n; ++i) {
		int x; scanf("%d", &x); f.push_back(x);
	}
	int inf = 1000000000;

	sort(f.begin(), f.end());

	int ans = n;
	for (int j = n; j > 0; --j) {
		int now = a, cnt = n - j;
		for (int i = 0; i < j; ++i) {
			while (now <= f[i]) {
				if (now == 1) {
					cnt = inf; break;
				}
				now = min(inf, now + now - 1); cnt++;
			}
			now = min(now + f[i], inf);
		}
		ans = min(ans, cnt);
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
