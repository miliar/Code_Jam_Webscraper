#include <iostream>
#include <string>

using namespace std;

int main () {
	int numTestCases;
	cin >> numTestCases;
	for (int i=0; i<numTestCases; ++i) {
		int k,m,n;
		cin >> k >> m >> n;
		int winner = 1;
		if (k<7) {
			if ((m*n) % k == 0) {
				if (k <= max(m,n)) {
					if (k<=2) {
						winner = 0;
					} else {
						if (k < 2 * (min(m,n) + 1) - 1) {
							if (k < min(m,n) + 1 + min(m,n) - 1) {
								winner = 0;
							}
						}
					}
				}
			}
		}
		if (winner == 1) {
			cout << "Case #" << (i+1) << ": " << "RICHARD" << endl; 
		} else {
			cout << "Case #" << (i+1) << ": " << "GABRIEL" << endl; 
		}
	}
}
