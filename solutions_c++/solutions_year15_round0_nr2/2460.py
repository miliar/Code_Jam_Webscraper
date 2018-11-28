#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T, D;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> D;
		int LIMIT = 0;
		vector<int> Q(D);
		for (int i = 0; i < D; i++) {
			cin >> Q[i];
			LIMIT = max(LIMIT, Q[i]);
		}
		int ans = LIMIT;
		for (int i = 1; i <= LIMIT; i++) {
			int delta = 0;
			for (int j = 0; j < D; j++) delta += (int)ceil(1.0 * Q[j] / i) - 1;
			ans = min(ans, i + delta);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
