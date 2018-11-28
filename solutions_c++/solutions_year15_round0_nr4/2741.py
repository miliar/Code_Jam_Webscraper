#include<iostream>

using namespace std;

int y, x, r, c;
bool w;

int main() {
	cin >> y;
	for (int z = 1; z <= y; z++) {
		cin >> x >> r >> c;
		if ((r * c) % x != 0) {
			w = false;
		}
		else if (x >= 7) {
			w = false;
		}
		else {
			if (x == 1) {
				w = true;
			}
			else if (x == 2) {
				w = true;
			}
			else if (x == 3) {
				if (max(r, c) <= 2) {
					w = false;
				}
				else if (min (r, c) == 1) {
					w = false;
				}
				else {
					w = true;
				}
			}
			else if (x == 4) {
				if (max(r, c) <= 3) {
					w = false;
				}
				else if (min(r, c) <= 2) {
					w = false;
				}
				else {
					w = true;
				}
			}
			else if (x == 5) {
				if (max(r, c) <= 4) {
					w = false;
				}
				else if (min(r, c) <= 2) {
					w = false;
				}
				else {
					w = true;
				}
			}
			else if (x == 6) {
				if (max(r, c) <= 5) {
					w = false;
				}
				else if (min(r, c) <= 3) {
					w = false;
				}
				else {
					w = true;
				}
			}
		}
		cout << "Case #" << z << ": ";
		if (w) {
			cout << "GABRIEL" << endl;
		}
		else {
			cout << "RICHARD" << endl;
		}
	}
}
