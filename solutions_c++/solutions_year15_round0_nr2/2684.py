#include <bits/stdc++.h>
using namespace std;

int n, a[100010];
int main() {
	int T; scanf("%d", &T); for(int ks = 1; ks <= T; ++ks) {
		int ans = 0, mx = 0;
		scanf("%d", &n); for(int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			mx = max(a[i], mx);
		}
		ans = mx;
		for(int i = 1; i <= mx; ++i) {
			int tmp = 0;
			for(int j = 0; j < n; ++j)
				tmp += (a[j] + i - 1) / i - 1;
			ans = min(ans, tmp + i);
		}
		printf("Case #%d: %d\n", ks, ans);
	}
	return 0;
}
