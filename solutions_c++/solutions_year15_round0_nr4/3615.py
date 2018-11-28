#include <iostream>
#include <string>

using namespace std;

template <typename T>
bool even(T num) {
	return (num & 1) == 0;
}
int main() {
	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; ++test) {
		int dimension, row, col;
		cin >> dimension >> row >> col;
		bool pick_fail = false;

		if (dimension == 1) pick_fail = false;
		else if (dimension == 2) {
			// even product can always win
			if (even(row * col)) pick_fail = false;
			else pick_fail = true;
		}
		else if (dimension == 3) {
			if (row == 1 || col == 1) pick_fail = true;
			else if (row < 3 && col < 3) pick_fail = true;
			else if (even(row) && even(col)) pick_fail = true;
			else pick_fail = false;
		}
		else if (dimension == 4) {
			// choose 2x2 omino
			if (row < 2 || col < 2) pick_fail = true;
			// choose 1x4
			else if (row < 4 && col < 4) pick_fail = true;
			else if ((row == 4 && col == 2) || (row == 2 && col == 4)) pick_fail = true;
			else pick_fail = false;
		}

		string winner = (pick_fail)? "RICHARD" : "GABRIEL";
		// if 
		cout << "Case #" << test << ": " << winner << endl;
	}

}