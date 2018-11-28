#include <bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		string s;
		cin >> s;
		int p = 0, m = 0, c = 0;
		bool plus = true;
		if (s[0] == '+')
			plus = false;
		for (int j = 0; j < s.size(); ++j) {
			if (s[j] == '+') {
				p++;
				if (!plus) {
					plus = true;
					c++;
				}
			} else {
				if (plus) {
					plus = false;
					c++;
				}
				m++;
			}
		}
		if (s[s.size() - 1] == '+')
			c--;
		cout << "Case #" << i + 1 << ": " << c << '\n';
	}
	return 0;
}
