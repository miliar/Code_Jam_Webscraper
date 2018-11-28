#include <bits/stdc++.h>

using namespace std;

vector <int> a;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, ans, n;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &n);
		a.clear();
		for (int i = 0; i < n; i++) {
			int t;
			scanf("%d", &t);
			a.push_back(t);
		}
		int mx = *max_element(a.begin(), a.end());
		int ans = mx;
		for (int i = 1; i < mx; i++) {
			int cur = i;
			for (int j = 0; j < a.size(); j++) {
				int t = a[j] / i - 1;
				if (a[j] % i != 0)
					t++;
				cur += t;
			}
			ans = min(ans, cur);
		}
		printf("Case #%d: %d\n", t, ans);
	}
}