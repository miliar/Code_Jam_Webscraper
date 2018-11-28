//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

bool solve(int x, int r, int c) {
	if (x == 1)
		return true;
	if (x == 2)
		return !(r % 2 == 1 && c % 2 == 1);
	if (x == 3)
		return (r == 2 && c == 3) || (r == 3 && c == 2) || (r == 3 && c == 3)
				|| (r == 3 && c == 4) || (r == 4 && c == 3);
	if (x == 4)
		return (r == 3 && c == 4) || (r == 4 && c == 3) || (r == 4 && c == 4);
	return false;
}
int main() {
	int T;
	int ca = 1;
	cin >> T;
	while (T--) {
		int x, r, c;
		cin >> x >> r >> c;
		string ans;
		if (solve(x, r, c)) {
			ans = "GABRIEL";
		} else {
			ans = "RICHARD";
		}
		cout << "Case #" << ca++ << ": " << ans << endl;
	}
	return 0;
}
