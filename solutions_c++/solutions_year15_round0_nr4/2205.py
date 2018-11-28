#include <iostream>
#include <algorithm>

using namespace std;

bool gabrielWon(unsigned x, unsigned r, unsigned c) {
	unsigned big = max(r,c);
	unsigned small = min(r,c);
	if (x >= 7) { // richard can choose an x-omino which has a single space in the middle, therefore will always win
		return false;
	}
	if ((x+1)/2 > small || x > big) { // richard can choose a piece that cannot fit in the box
		return false;
	}
	if (x > 3 && (x+1)/2 == small) {
		return false;
	}
	if ((r*c) % x == 0) { // gabriel can pick pieces to fit around the forced one
		return true;
	}
	return false;
}

int main() {
	unsigned t;
	cin >> t;
	for (unsigned caseNum = 1; caseNum <= t; caseNum++) {
		unsigned x, r, c;
		cin >> x;
		cin >> r;
		cin >> c;
		cout << "Case #" << caseNum << ": ";
		if (gabrielWon(x,r,c)) {
			cout << "GABRIEL\n";
		} else {
			cout << "RICHARD\n";
		}
	}
	return 0;
}