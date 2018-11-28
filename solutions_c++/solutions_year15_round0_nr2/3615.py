#include <bits/stdc++.h>
using namespace std;

int P[1005];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;

	for (int tc = 1 ; tc <= T ; tc ++){
		int D, DD, ans = 1<<28, maxi = 0 ;
		cin >> D;
		for (int i = 0 ; i < D ; i ++){
			cin >> P[i];
			maxi = max(maxi, P[i]);
		}
		DD = maxi;
		for (int mx = 1 ; mx <= DD ; mx ++){
			int ret = mx;
			for (int i = 0 ; i < D ; i ++){
				if (P[i] <= mx) continue;
				ret += (P[i]/mx) + !!(P[i]%mx) - 1;
			}
			ans = min(ret, ans);
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}
