#include <bits/stdc++.h>
using namespace std;

int p[1111];

int main(void) {


	int cases; scanf("%d", &cases);
	int cas = 0;
	while (cases--) {
	
		printf("Case #%d: ", ++cas);
		
		int n = 0; scanf("%d", &n);

		int Max = 0;
		
		for (int i = 0; i < n; ++i) {
			scanf("%d", &p[i]);
			Max = max(Max, p[i]);
		}

		int ans = 1111;
		
		for (int last = 1; last <= Max; ++last) {
		
			int spec = 0;
		
			for (int i = 0; i < n; ++i) {
				if (p[i] < last) continue;
				spec += (p[i] - 1) / last;
			}
			ans = min(ans, spec+last);
		}
	
		printf("%d\n", ans);
	
	}

	return 0;
}
