#include<bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	t++;
	string s;
	getline(cin, s);
	vector<bool> a;
	for (int tc = 1; tc < t; ++tc) {
		cout << "Case #" << tc << ": ";
		getline(cin, s);
		a.resize(s.size());
		for (int i = 0; i < s.size(); ++i) {
			a[i] = (s[i] =='+');
		}
		int ansm = 0;
		int ansp = 0;
		for (int i = 0; i < a.size(); ++i) {
			if (!a[i]) {
				ansp = ansm + 1;
			} else {
				ansm = ansp + 1;
			}
		}
		cout << ansp << "\n";
	}
}
