#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; ++i) {
		int acc = 0, ans = 0;
		int n;
		string s;
		cin >> n >> s;
		for (int i = 0; i < s.size(); ++i) {
			ans = max(ans, i - acc);
			acc += s[i] - '0';
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
