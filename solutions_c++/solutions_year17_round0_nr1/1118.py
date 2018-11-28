#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#define int long long
using namespace std;

signed main() {
	int tc; cin >> tc;
	for(int t = 1; t <= tc; ++t) {
		string s; int k; cin >> s >> k;
		int n = s.size();
		int ans = 0;
		for(int i = 0; i+k <= n; ++i) {
			if(s[i] == '-') {
				++ans;
				for(int j = i; j < i+k; ++j) {
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
			// cout << s << endl;
		}
		printf("Case #%lld: ", t);
		bool okay = true;
		for(int i = 0; i < n; ++i) {
			if(s[i] == '-') {
				okay = false;
				cout << "IMPOSSIBLE" << endl;
				break;
			}
		}
		if(okay) cout << ans << endl;
	}
}
