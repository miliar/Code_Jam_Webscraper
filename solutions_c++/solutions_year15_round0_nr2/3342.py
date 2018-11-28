#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1010;
int t, d, p[MAXN];

int main() {
	scanf("%d", &t);
	int xx = 1;
	while (t--) {
		scanf("%d", &d);
		for (int i = 0; i < d; i++) scanf("%d", &p[i]);
		int ans = INT_MAX;
		for (int i = 1; i <= 1000; i++) {
			int cnt = 0;
			for (int j = 0; j < d; j++) {
				cnt += (p[j] - 1) / i;
			}
			ans = min(ans, cnt + i);
		}
		printf("Case #%d: %d\n", xx++, ans);
	}
	return 0;
}
