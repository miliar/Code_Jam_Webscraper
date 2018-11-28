#include <bits/stdc++.h>
#define N 1000
using namespace std;

int p[N];

int main() {
	int t; scanf("%d", &t);
	for (int T = 0; T < t; ++T) {
		int d; scanf("%d", &d);
		for (int i = 0; i < d; ++i) {
			scanf("%d", p + i);
		}
		int up = *max_element(p, p + d);
		int ans = up;
		for (int mx = 1; mx <= up; ++mx) {
			int cnt = 0;
			for (int i = 0; i < d; ++i) {
				if (p[i] > mx) {
					cnt += (p[i] + mx - 1) / mx - 1;
				}
			}
			ans = min(ans, mx + cnt);
		}
		printf("Case #%d: %d\n", T + 1, ans);
	}
	return 0;
}
