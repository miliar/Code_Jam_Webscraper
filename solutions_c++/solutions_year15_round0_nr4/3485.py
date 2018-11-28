#include <bits/stdc++.h>

using namespace std;

int main() {

	int T;
	cin >> T;

	for (int i = 0; i <T; i++) {

		int X, R, C;
		cin >> X >> R >> C;
		
		cout << "Case #" << i + 1 << ": ";

		if ((R * C - X) % X != 0) cout << "RICHARD" << endl;
		else if (R == 1 && C == 1 && X > 1) cout << "RICHARD" << endl;
		else if ((R == 1 || C == 1) && X > 2) cout << "RICHARD" << endl;
		else cout << "GABRIEL" << endl;
	}
}