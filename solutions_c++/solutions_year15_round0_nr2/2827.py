#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int T, n, ans;
int a[1001];

int main() {
	freopen("2.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
		ans = 1001;
		for (int i = 1; i <= 1000; ++i) {
			int t = i;
			for (int j = 1; j <= n; ++j) t += (a[j] - 1) / i;
			ans = min(ans, t);
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
