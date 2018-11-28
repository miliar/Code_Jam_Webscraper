#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("A.txt", "wt", stdout);
#endif

	int T;
	string s;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> s;
		if (s.size()) {
			string sol = "";
			sol += s[0];
			for (int i = 1; i < s.size(); i++) {
				if (sol[0] <= s[i]) {
					sol = s[i] + sol;
				} else
					sol += s[i];
			}
			cout << "Case #" << t + 1 << ": " << sol << endl;
		}
	}
	return 0;
}

