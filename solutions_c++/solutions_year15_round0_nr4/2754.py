#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
	int i, j, k;
	int rnds, cnt, result;
	int x, r, c;
	char in;
	int a[2000];

	cin >> rnds;
	for (int ii = 0; ii < rnds; ii++) {
		cin >> x >> r >> c;
		result = 0;
		if ((r * c) % x != 0) {
			result = 1;
		}
		else if (x > r * c) {
			result  = 1;
		}
		else if (x > 2 && x == r * c) {
			result = 1;
		}
		else if (x == 4) {
			if (r * c == 8) {
				result = 1;
			}
		}


		if (result == 0) {
			cout << "Case #" << (ii + 1) << ": " << "GABRIEL" << endl;
		}
		else {
			cout << "Case #" << (ii + 1) << ": " << "RICHARD" << endl;
		}
	}


	return 0;
}



