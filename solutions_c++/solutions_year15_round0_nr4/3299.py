#include <iostream>
#include <string>
using namespace std;
void cas() {
	int x, r, c; cin >> x >> r >> c;
	if ((x > r && x > c) || r * c % x) {
		cout << "RICHARD" << endl;
		return;
	}
	if ((r == 1 || c == 1) && x > 2) {
		cout << "RICHARD" << endl;
		return;
	}
	if (x < 4) {
		cout << "GABRIEL" << endl;
		return;
	}
	if (r < 3 || c < 3)
		cout << "RICHARD" << endl;
	else
		cout << "GABRIEL" << endl;
}
int main() {
	int t; cin >> t;
	int x = 1; while (t--) {
		cout << "Case #" << x++ << ": ";
		cas();
	}
}
