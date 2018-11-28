#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	cin >> T;
	while (T--) {
		int ans;
		int maxi;
		string s;
		cin >> maxi >> s;
		for (ans = 0; ans <= 1000; ++ans) {
			int cur = ans + s[0] - '0';
			bool good = true;
			for (int i = 1; i < maxi + 1; ++i) {
				if (s[i] == '0') continue;
				if (cur < i) {
					good = false;
					break;
				}
				cur += s[i] - '0';
			}
			if (good) goto END;
		}

		END:
		cout << "Case #" << K++ << ": " << ans << endl;
	}
	return 0;
}
