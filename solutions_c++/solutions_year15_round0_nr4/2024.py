#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int t1 = 1; t1 <= t; t1++) {
		int x, r, c;
		cin >> x >> r >> c;
		cout << "Case #" << t1 << ": ";
		switch (x) {
			case 1: cout << "GABRIEL" << endl; break;
			case 2:
				if ((r * c) % 2 == 0)
					cout << "GABRIEL";
				else
					cout << "RICHARD"; break;
			case 3:
				if (r >= 2 && c >= 2 && (r * c) % 3 == 0)
					cout << "GABRIEL";
				else
					cout << "RICHARD"; break;
			case 4:
				if (r >= 3 && c >= 3 && (r * c) % 4 == 0)
					cout << "GABRIEL";
				else
					cout << "RICHARD"; break;
		}
		cout << endl;
	}
}
