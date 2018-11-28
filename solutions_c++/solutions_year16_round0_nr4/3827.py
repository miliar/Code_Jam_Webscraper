/*
 * c.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: nmarwan
 */


#include <iostream>

using namespace std;

long long pw (long long b, long long p) {
	if (p == 0) return 1;
	return pw(b, p-1) * b;
}

int main () {
	freopen("c.i", "rt", stdin);
	freopen("c.o", "wt", stdout);

	int t;
	cin >> t;
	for (int tt = 1 ; tt <= t ; tt++) {
		cout << "Case #" << tt << ": ";
		long long k, c, s;
		cin >> k >> c >> s;

		if (c == 1) {
			if (s < k) {
				cout << "IMPOSSIBLE" << endl;
			}else {
				for (int i=1 ; i <= k ; i++) {
					cout << i << " ";
				}
				cout << endl;

			}
			continue;
		}

		if (s < (k+1)/2) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		for (int i=0, offset = 1 ; i < k ; i+=2, offset+=2) {
			cout << min(i*pw(k , c-1) + offset+1, pw(k,c)) << " ";
		}
		cout << endl;
	}


	return 0;
}


