#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	ifstream fin("input.in");
	ofstream fout("output.out");
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	int T, n, c, first, last, ans;
	fin >> T;
	string s;
	for (int t = 1; t <= T; t++) {
		fin >> s;
		fout << "Case #" << t << ": ";
		n = s.length();
		c = 0;
		first = -1;
		last = n - 1;
		vector < int > x(n);
		ans = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == '-') {
				x[i] = 0;
			} else {
				x[i] = 1;
				c++;
			}
		}
		if (c == n) {
			fout << "0" << endl;
		} else {
			while (c != n) {
				for (int i = n - 1; i >= 0; i--) {
					if (x[i] == 0) {
						last = i;
						break;
					}
				}
				for (int i = 0; i < n; i++) {
					if (x[i] == 0) {
						first = i;
						break;
					}
				}
				if (first > 0) {
					for (int i = 0; i <= first / 2; i++) {
						swap(x[i], x[first - 1 - i]);
					}
					for (int i = 0; i < first; i++) {
						x[i] = 1 - x[i];
					}
					ans++;
				}
				for (int i = 0; i <= last / 2; i++) {
					swap(x[i], x[last - i]);
				}
				for (int i = 0; i <= last; i++) {
					x[i] = 1 - x[i];
				}
				ans++;
				c = 0;
				for (int i = 0; i < n; i++) {
					if (x[i] == 1) {
						c++;
					}
				}
			}
			fout << ans << endl;
		}
	}
	return 0;
}