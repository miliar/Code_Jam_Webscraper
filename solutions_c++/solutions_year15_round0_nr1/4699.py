#include <bits/stdc++.h>
using namespace std;

int main() {
	int T, t, n, i, a, r;
	string s;
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	cin >> T;
	for (t = 1; t <= T; t++) {
		a = r = 0;
		cin >> n >> s;
		for (i = 0; i <= n; i++) {
			if (a < i) {
				r += i - a;
				a = i;
			}
			a += s[i] - '0';
		}
		cout << "Case #" << t << ": " << r << '\n';
	}
	return 0;
}