#include <iostream>

// Gilles Waeber, 12.04.2015

using namespace std;

// CAN ALWAYS BE FILLED ?
bool answer(){
	int X, R, C;
	cin >> X >> R >> C;
	if (X >= 7) return false; // hole

	if ((R * C) % X) return false; // we don't have half-xominos

	if (R < C) swap(R, C); // R >= C

	if (X == 1) return true;
	if (X == 2) return true; // 1x1 eliminied by mod
	if (X == 3) return R >= 3 && C >= 2;
	if (X == 4) return R >= 4 && C >= 3;
	if (X == 5) return R >= 5 && C >= 4;
	if (X == 6) return R >= 6 && C >= 4;

	// we should not arrive here
	return false;
}

// B. INFINITE HOUSE OF PANCAKES

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ": " << (answer() ? "GABRIEL" : "RICHARD") << "\n";
	}
	cout << flush;
}