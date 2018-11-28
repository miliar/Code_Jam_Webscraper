#include <bits/stdc++.h>
using namespace std;

void run() {
	string s; cin >> s;
	int k; cin >> k;
	int res = 0;
	for (int i = 0; i + k <= (int) s.size(); ++i) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; ++j) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
			++res;
		}
	}
	if (s == string(s.size(), '+')) cout << res;
	else cout << "IMPOSSIBLE";
}

int main() {
	int nt; cin >> nt;
	for (int i = 0; i < nt; ++i) {
		cout << "Case #" << i + 1 << ": ";
		run();
		cout << '\n';
	}
	return 0;
}
