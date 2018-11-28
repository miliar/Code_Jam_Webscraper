#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

const int MAX_N = 1010;
map<int, int> mp;
int a[MAX_N], b[MAX_N], n;

int main() {
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		int ans = 0;
		scanf("%d", &n);
		mp.clear();
		for (int i = 0; i < n; i++) {
			scanf("%d", a + i);
			b[i] = a[i];
		}
		sort(b, b + n);
		for (int i = 0; i < n; i++) {
			mp[b[i]] = i;
		}
		for (int i = 0; i < n; i++) {
			a[i] = mp[a[i]];
		}
		for (int i = 0; i < n; i++) {
			int w = -1;
			for (int j = 0; j < n; j++) {
				if (a[j] == i) {
					w = j;
					break;
				}
			}
			int a1 = 0, a2 = 0;
			for (int j = w - 1; j >= 0; j--) {
				if (a[j] > i) {
					a1++;
				}
			}
			for (int j = w + 1; j < n; j++) {
				if (a[j] > i) {
					a2++;
				}
			}
			ans += min(a1, a2);
		}
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}
