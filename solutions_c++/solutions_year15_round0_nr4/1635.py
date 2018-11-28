
#include <iostream>

using namespace std;

int mins[] = {0, 1, 1, 2, 3};

bool win(int X, int R, int C) {
	if (R < C) return win(X, C, R);

	// guaranteed to R >= C
	//cout << X << ' ' << R << ' ' << C << " -> ";
	if ((R * C) % X != 0) return true;
	if (X > R) return true;
	if (C < mins[X]) return true;
	
	return false;
}

int main() {
	int T, X, R, C;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> X >> R >> C;
		cout << "Case #" << t << ": " << (win(X, R, C) ? "RICHARD" : "GABRIEL") << endl;
	}

	return 0;
}

