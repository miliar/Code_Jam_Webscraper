/*
 * d.cpp
 *
 *  Created on: 11-Apr-2015
 *      Author: akshay
 *  If one of these conditions is false, Richard wins:
 *  1. R * C must be a multiple of X : Otherwise it is impossible to fill the rectangle with X-ominoes
 *  2. R >= X or C >= X : Otherwise Richard can select a straight line to defeat Gabriel
 *  3. R >= ceil(X/2.0) and C >= ceil(X/2.0) : Otherwise Richard can choose an angled piece of size
 *  	(floor(X/2.0) + 1, ceil(X/2.0)) to win
 *  4. If X is even and R == ceil(X/2.0) or C == ceil(X/2.0), it is possible to choose a T-like piece
 *  	with width floor(X/2.0) + 1 and height ceil(X/2.0) to split the grid so that the number of cells
 *  	on neither side is a multiple of X. Moreover, the X-omino cannot be rotated
 *  5. Special case 2 1 4 : Richard has only one option and Gabriel can plug in the remaining space with the same piece.
 *  Since angle and T are not possible in this case, the corresponding checks are irrelevant.
 */

#include <iostream>
#include <cmath>

#define RICHARD "RICHARD"
#define GABRIEL "GABRIEL"

using namespace std;

int main() {
	int t;

	cin >> t;

	for(int tc = 0; tc < t; tc++) {
		int x, r, c;
		const char* winner;

		cin >> x >> r >> c;

		cerr << x << " " << r << " " << c << endl;
		int min = x / 2 + 1;
		if((r * c) % x == 0 && (x < 3 ||
				((r >= min && c >= min) &&
						(r >= x || c >= x)))) {
			winner = GABRIEL;
		} else {
			winner = RICHARD;
		}

		cout << "Case #" << (tc + 1) << ": " << winner << endl;
	}

	return 0;
}
