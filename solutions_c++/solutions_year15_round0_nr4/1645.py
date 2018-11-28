#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int j = 1; j <= T; ++j) {
		int X, R, C;
		cin >> X >> R >> C;
		bool rwin = false;
		if (X >= 7) {
			rwin = true;
		} else if ((R*C)%X > 0) {
			rwin = true;
		} else if ((X+1)/2 > min(R, C)){
			rwin = true;
		} else if (X > R + C - 1) {
			rwin = true;
		} else if (X == 4 && min(R, C) < 3) {
			rwin = true;
		} else if (X > max(R, C)) {
			rwin = true;
		} else if (X == 6 && min(R, C) < 4) {
			rwin = true;
		}
		cout << "Case #" << j << ": " << (rwin ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}

