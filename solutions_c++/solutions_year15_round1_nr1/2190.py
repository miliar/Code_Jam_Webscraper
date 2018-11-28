#include <bits/stdc++.h>

using namespace std;

int a[1111];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t, tst = 1;
	scanf("%d", &t);
	while (t--) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", a + i);
		long long ans1 = 0;
		int mx = 0;
		for (int i = 1; i < n; ++i) {
			if (a[i] < a[i - 1]) {
				ans1 += a[i - 1] - a[i];
				mx = max(mx, a[i - 1] - a[i]);
			}
		}
		// int rate = (mx + 9) / 10;
		long long ans2 = 0;
		for (int i = 0; i + 1 < n; ++i) {
			ans2 += min(a[i], mx);
		}
		printf("Case #%d: %lld %lld\n", tst, ans1, ans2);
		++tst;
	}
}