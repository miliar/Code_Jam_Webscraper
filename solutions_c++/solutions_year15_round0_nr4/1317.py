#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	string g = "GABRIEL";
	string rc = "RICHARD";
	for (int t=1;t<=T;t++) {
		int x, r, c;
		cin >> x;
		cin >> r;
		cin >> c;
		cout << "Case #" << t << ": ";

		if ( x >= 7) {
			cout << rc << endl;
			continue;
		} else if (x == 1) {
			cout << g << endl;
			continue;
		} else if (x == 2) {
			if ( (r*c) % x == 0) {
				cout << g << endl;
			} else {
				cout << rc << endl;
			}
			continue;
		} else if (x == 3) {
			if ( (r*c) % x == 0 && (r >= 2 && c >= 2)) {
				cout << g << endl;
			} else {
				cout << rc << endl;
			}
			continue;
		}
		// 4 or 5 or 6
		if ( (r*c) % x != 0 || (r*c) == x) {
			cout << rc << endl;
			continue;
		}
		if ( r <= 2 || c <= 2) {
			cout << rc << endl;
			continue;
		}
		if ( x == 6 && (r <= 3 || c <= 3)) {
			cout << rc << endl;
			continue;
		}
		cout << g << endl;
	}
	return 0;
}
