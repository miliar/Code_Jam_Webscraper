/*
 * Standing Ovation.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: mohamed265
 */

#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, sMax, slon, st;
	string des;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		st = slon = 0;
		cin >> sMax >> des;
		for (int j = 0; j < sMax + 1; ++j) {

			if (des[j] != '0') {
				if (st < j) {
					slon += (j - st);
					st = j;
				}
				st += (des[j] - '0');
			}
			//	cout << st << ' ' << slon << endl;
		}
		cout << "Case #" << i + 1 << ": " << slon << endl;
	}

	return 0;
}
