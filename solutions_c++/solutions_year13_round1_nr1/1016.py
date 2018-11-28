//============================================================================
// Name        : bullseye.cpp
// Author      : swem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int caseIdx = 1; caseIdx <= t; caseIdx++) {
		long long int r, t;
		cin >> r >> t;
		// the first black ring: (r+1)^2-r^2
		// the first 1~k black ring: 2k^2 + (2*r-1)*k (unit area)

		long long int a = 0;
		long long int b = min((long long int) floor(sqrt(t / 2)),
				t / (2 * r - 1)) + 1;
		//binary search
		while (b - a > 1) {
			long long int k = (a + b) / 2;
			if ((2 * k * k + (2 * r - 1) * k) <= t) {
				a = k;
			} else {
				b = k;
			}
		}
		cout << "Case #" << caseIdx << ": " << a << endl;
	}
	return 0;
}
