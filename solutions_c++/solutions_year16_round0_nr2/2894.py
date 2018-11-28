#include <bits/stdc++.h>
using namespace std;

main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int _ = 1; _ <= T; ++_) {
		string s;
		cin >> s;
		int x = 1;
		for (int i = 1; i < s.size(); ++i)
			if (s[i] != s[i - 1])
				x ++;
		if (s[s.size() - 1] == '+')
			x --;
		cout << "Case #" << _ << ": " << x << '\n';
	}
	return 0;
}

