#include <iostream>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
	int T; cin >> T;
	int t = 1;
	while (t <= T) {
		cout << "Case #" << t++ << ": ";
		
		int X, R, C;
		cin >> X >> R >> C;
		
		if (X == 1) {
			cout << "GABRIEL" << endl;
		} else if ((R*C)%X != 0) {
			cout << "RICHARD" << endl;
		} else if (X == 2) {
			cout << "GABRIEL" << endl;
		} else if (R*C == 3) {
			cout << "RICHARD" << endl;
		} else if (X == 3) {
			cout << "GABRIEL" << endl;
		} else if (R*C == 4 || R*C == 8) {
			cout << "RICHARD" << endl;
		} else {
			cout << "GABRIEL" << endl;
		}
	}
	return 0;
}
