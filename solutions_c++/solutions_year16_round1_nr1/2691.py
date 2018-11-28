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
		deque <char> d(1, s[0]);
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] >= d.front())
				d.push_front(s[i]);
			else d.push_back(s[i]);
		}
		for (int i = 0; i < d.size(); ++i) {
			cout << d[i];
		}
		puts("");
	}
    return 0;
}