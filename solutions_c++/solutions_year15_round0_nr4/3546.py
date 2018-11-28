#include<iostream>
using namespace std;

int main() {
	int i, j, t, x, r, c;

	cin >> t;

	for(i = 0; i < t; i++) {
		cin >> x >> r	>> c;
		cout << "Case #" << (i + 1) << ": ";

		if((r >= (x - 1)) && (c >= (x - 1)) && (((r * c) % x ) == 0)) {
			cout << "GABRIEL\n";
		} else {
			cout << "RICHARD\n";
		}
	}
}
