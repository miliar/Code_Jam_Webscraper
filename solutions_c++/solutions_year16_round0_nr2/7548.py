#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
	freopen("inp.txt", "r", stdin);
	freopen("outp.txt", "w", stdout);
#endif
    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
		cout << "Case #" << c << ": ";
		string s;
		cin >> s;
		int ans = 1;
		for (int i = 1; i < s.size(); ++i)
			if (s[i] != s[i - 1])
				++ans;
		cout << ans - (s[s.size() - 1] == '+') << endl;
    }
	return 0;
}