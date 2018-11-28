#include<bits/stdc++.h>
using namespace std;

void __main() {
	string s;
	cin >> s;
	int ans = 0;
	if (s[0] == '-') {
		ans++;
	}
	int n = s.size();
	for (int i = 1; i < n; ++i) {
		if (s[i] == '-' && s[i] != s[i - 1]) {
			ans += 2;
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		printf("Case #%d: ", testcase);
		__main();
	}
	return 0;
}
