#include <iostream>

using namespace std;

bool check(int x, int r, int c) {
	if (r*c%x != 0) return false;
	if (r > c) {
		int temp = r;
		r = c;
		c = temp;
	}
	if (x == 1) return true;
	if (x == 2) return true;
	if (x == 3) {
		if (r == 1) return false;
		else return true;
	}
	if (x == 4) { 
		if (r <= 2) return false;
		else return true;
	}
}

int solve(int test) {
	int x, r, c;
	cin >> x >> r >> c;
	if (check(x, r, c)) {
		cout << "Case #" << test << ": " << "GABRIEL" << endl;
	} else {
		cout << "Case #" << test << ": " << "RICHARD" << endl;
	}

	return 0;
}

int main() {
	int test;
	cin >> test;
	for (int t = 0; t < test; t++) {
		solve(t+1);
	}
	return 0;
}
