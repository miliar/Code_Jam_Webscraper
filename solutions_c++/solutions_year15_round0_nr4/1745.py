#include <iostream>

using namespace std;


bool CanSolve(int X, int R, int C) {
	if ((R * C) % X != 0) {
		return false;
	}
	if (X == 1 || X == 2) {
		return true;
	}
	int level = (X - 1) / 2 + 1;
	if (X % 2 == 0) {
		level ++;
	}
	if (min(R, C) < level) {
		return false;
	}
	return true;
}


int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int X;
		cin >> X;
		int R;
		cin >> R;
		int C;
		cin >> C;

		cout << "Case #" << i + 1 << ": ";
		if (CanSolve(X, R, C))  {
			cout << "GABRIEL" << endl;
		} else {
			cout << "RICHARD" << endl;
		}
		
	}
	return 0;
}