#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;

	for (int casenum = 0; casenum < t; casenum++) {
		unsigned long long k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << casenum+1 << ": ";

		// assume S = K
		unsigned long long diff = 1;
		unsigned long long curpow = 1;
		for (unsigned long long i = 1; i < c; i++) {
			curpow *= k;
			diff += curpow;
		}

		cout << "1";
		unsigned long long cur = 1 + diff;
		for (unsigned long long i = 1; i < s; i++) {
			cout << " " << cur;
			cur += diff;
		}
		cout << endl;
	}
	return 0;
}
