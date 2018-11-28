#include <bits/stdc++.h>
using namespace std;

int main() {
	int T, d, p[1005];
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		scanf("%d", &d);
		for(int i = 0; i < d; i++)
			scanf("%d", &p[i]);
		int ans = 0, tmp;
		for(int i = 0; i < d; i++)  ans = max(ans, p[i]);
		for(int i = 1; i <= 1000; i++) {
			tmp = 0;
			int ii = 0;
			for(int j = 0; j < d; j++) {
				if(p[j] > i) {
					tmp += (p[j] - 1) / i;
					ii = i;
				}
				else  ii = max(ii, p[j]);
			}
			ans = min(ans, tmp + ii);
		}
		printf("%d\n", ans);
	}
	return 0;
}
