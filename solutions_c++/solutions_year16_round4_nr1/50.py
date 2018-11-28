#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string calc(int winner, int n) {
	if (n == 0) {
		return string(1, "PRS"[winner]);
	} else {
		string a = calc(winner, n - 1);
		string b = calc((winner + 1) % 3, n - 1);
		if (a < b)
			return a + b;
		else
			return b + a;
	}
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		string calc_res[3] = {calc(0, n), calc(1, n), calc(2, n)};
		string ans = "ZZZ";
		/*
		for (int i = 0; i < 3; i++)
			cout << calc_res[i] << endl;
			*/
		for (int i = 0; i < 3; i++) {
			string &str = calc_res[i];
			bool ok = 
				r == count(str.begin(), str.end(), 'R') &&
				p == count(str.begin(), str.end(), 'P') &&
				s == count(str.begin(), str.end(), 'S');

			if (ok && ans > str)
				ans = str;
		}

		cout << "Case #" << t << ": ";
		// print the answer
		if (ans == "ZZZ")
			cout << "IMPOSSIBLE" << endl;
		else 
			cout << ans << endl;
	}

	return 0;
}
