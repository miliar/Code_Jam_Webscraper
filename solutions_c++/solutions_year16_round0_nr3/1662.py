#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;

	for (int casenum = 0; casenum < t; casenum++) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << casenum+1 << ":" << endl;
		int a = 2 * (n % 2), b = 0;
		// print it out like ABABABABA
		int output = 0; // number of output

		int truncatedn = n-2;

		int alen = truncatedn/2 + (n % 2), blen = truncatedn/2;

		int aarr[alen], barr[blen];

		while (a <= (n - 1) / 2) {
			fill(aarr, aarr + alen - a, 0);
			fill(aarr + alen - a, aarr + alen, 1);
			fill(barr, barr + blen - b, 0);
			fill(barr + blen - b, barr + blen, 1);
			// cerr << "aarr is ";
			// for (int i = 0; i < alen; i++) {
			// 	cerr << aarr[i] << " ";
			// }
			// cerr << endl;
			// cerr << "barr is ";
			// for (int i = 0; i < blen; i++) {
			// 	cerr << barr[i] << " ";
			// }
			// cerr << endl;
			do {
				do {
					cout << 1;
					for (int i = 0; i < truncatedn; i++) {
						if (i % 2 == 0) {
							cout << aarr[i/2];
						} else{
							cout << barr[i/2];
						}
					}
					cout << 1 << " 3 4 5 6 7 8 9 10 11" << endl;
					output++;
					if (output == j) {
						goto stop;
					}
				} while (next_permutation(barr, barr + blen));
			} while (next_permutation(aarr, aarr + alen));

			a++;
			b++;
		}
		stop:;
	}

	// int x[] = {0, 0, 0, 1, 1};
	// do {
	// 	for (int i = 0; i < 5; i++) {
	// 		cout << x[i] << " ";
	// 	}
	// 	cout << endl;
	// } while (next_permutation(x, x+5));
	return 0;
}
