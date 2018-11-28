#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 1005;

int a[N];

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		int ans = 1000, n;
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
		for (int i = 1; i <= 1000; ++i) {
			int tmp = 0;
			for (int j = 1; j <= n; ++j) {
				tmp += (a[j] - 1) / i;
			}
			ans = min(ans, tmp + i);
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}

