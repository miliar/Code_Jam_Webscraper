#include <bits/stdc++.h>
using namespace std;

int t, s;
char str[1010];

int main() {
	scanf("%d", &t);
	int xx = 1;
	while (t--) {
		scanf("%d%s", &s, str);
		int lo = 0, hi = 1010, ans = -1, mid;
		while (lo <= hi) {
			mid = (lo + hi) >> 1;
			int ppl = mid;
			bool ok = true;
			for (int i = 0; i <= s; i++) {
				if (ppl >= i) {
					ppl += (int)(str[i] - '0');
				} else {
					ok = false; break;
				}
			}
			if (ok) {
				ans = mid;
				hi = mid - 1;
			} else lo = mid + 1;
		}
		printf("Case #%d: %d\n", xx++, ans);
	}
	return 0;
}
