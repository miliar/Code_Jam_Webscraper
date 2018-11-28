/*
 * Omino.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: ngoyal
 */

#include<iostream>
#include<math.h>
using namespace std;

int solve(int X, int R, int C) {
	if ((R * C) % X != 0)
		return 0;
	if (floor((X + 1) / 2) > min(R, C))
		return 0;
	if (X == 4 && R == 2 && C == 4)
		return 0;
	if (X == 4 && R == 4 && C == 2)
		return 0;
	if (X == 4 && R == 2 && C == 2)
		return 0;
	return 1;
}

int main() {
	int T;
	int caseNo = 1;
	cin >> T;
	while (T--) {
		int X, R, C;
		cin >> X;
		cin >> R;
		cin >> C;
		int result = solve(X, R, C);
		if (result == 1)
			cout << "Case #" << caseNo << ": GABRIEL\n";
		else
			cout << "Case #" << caseNo << ": RICHARD\n";
		caseNo++;
	}
}
