#include <iostream>
#include <set>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int t;

	cin >> t;
	string s;
	for (int tt = 1; tt <= t; tt++) {
		cin >> s;
		cout << "Case #" << tt <<": ";
		string res = "";
		res +=s[0];
		for (int i = 1; i < s.size(); i++) {
			if (s[i] < res[0]) {
				res+=s[i];
			} else {
				res = s[i] + res;
			}
		}
		cout << res << endl;
	}
	return 0;
}
