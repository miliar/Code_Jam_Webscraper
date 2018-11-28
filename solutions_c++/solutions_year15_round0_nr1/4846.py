/*/**/

#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	int cnt = 1;
	while(t--) {
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0;
		int now = s[0] - '0';
		for(int i = 1; i <= n; i++) {
			if(s[i] - '0') {
				if(now >= i) {
					now += s[i] - '0';
				}
				else {
					int diff = i - now;
					ans += diff;
					now += diff + s[i] - '0';
				}
			}
		}
		printf("Case #%d: %d\n", cnt++, ans);
	}
	return 0;
}