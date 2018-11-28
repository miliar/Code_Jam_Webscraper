#include <iostream>
using namespace std;

int main() {
	int t, x, r, c;
	bool flag = true;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		cin >> x >> r >> c;
		if (c < r) {
			r ^= c; c ^= r; r ^= c;
		}
		switch(x) {
			case 1: flag = false; break;
			case 2: flag = (r&1) && (c&1); break;
			case 3: 
			switch(r) {
				case 1: flag = true; break;
				case 2: flag = (c != 3); break;
				case 3: flag = false; break;
				case 4: flag = true; break;
			}
			break;
			case 4: flag = !(r >= 3 && c == 4); break;
		}
		cout << "Case #" << tt << ": ";
		if (flag) 
			cout << "RICHARD";
		else 
			cout << "GABRIEL";
		cout << endl;
	}
	return 0;
}