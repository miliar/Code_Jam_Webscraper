#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;


int main() {
	ofstream cout("out.txt");
	ifstream cin("in.in");
	int T;
	cin >> T;
	for (int idx = 1; idx <= T; idx++) {
		int x, R, C;
		cin >> x >> R >> C;
		int r = min(R, C);
		int c = max(R, C);
		if (x == 1)
			cout << "Case #" << idx << ": GABRIEL\n";
		else if (x == 2) {
			if (r*c % 2)
				cout << "Case #" << idx << ": RICHARD\n";
			else
				cout << "Case #" << idx << ": GABRIEL\n";
		}
		else if (x == 3) {
			if (r == 1 || r == 4 || (r==2 && (c == 4 || c == 2)))
				cout << "Case #" << idx << ": RICHARD\n";
			else
				cout << "Case #" << idx << ": GABRIEL\n";
		}
		else if (x == 4) {
			if (r == 1 || r == 2 || (r == 3 && c == 3) )
				cout << "Case #" << idx << ": RICHARD\n";
			else
				cout << "Case #" << idx << ": GABRIEL\n";
		}
	}
	return 0;
}