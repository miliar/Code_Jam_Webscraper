#include <bits/stdc++.h>

using namespace std;

#define size(s) (int) (s).size()

int main() {
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int t, it = 1;
	cin >> t;
	while (t) {
		cout << "Case #" << it << ": ";
		string s;
		int cnt = 1;
		cin >> s;
		for (int i = 1; i < size(s); i++) {
			if (s[i] != s[i - 1]) {
				cnt++;
			}
		}
		if (s[size(s) - 1] == '+') {
			cnt--;
		}
		cout << cnt << '\n';
		it++;
		t--;
	}
	return 0;
}