#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int caso = 1; caso <= t; caso++) {
		long long int ans = 0;
		long long int cur = 0;
		int n;
		string s;
		cin >> n >> s;
		for (long long int k = 0; k <= n; k++) {
			long long int d = s[k] - '0';
			if (cur < k) {
				ans += (k - cur);
				cur = k;
			}
			cur += d;
		}
		printf("Case #%d: %lld\n", caso, ans);
	}
	return 0;
}

