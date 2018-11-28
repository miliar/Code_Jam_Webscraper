#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T, k, cases = 0;
	string p;
	cin >> T;
	while(T--) {
		cin >> p >> k;
		int n = p.length();
		int ans = 0;
		for(int i = 0; i + k <= n; i++) {
			if(p[i] == '-') {
				for(int j = i; j < i + k; j++)
					if(p[j] == '-') p[j] = '+'; else p[j] = '-';
				ans++;
			}
		}
		for(int i = 0; i < n; i++) if(p[i] == '-') ans = -1;
		printf("Case #%d: ", ++cases);
		if(ans < 0) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
	}
	return 0;
}
