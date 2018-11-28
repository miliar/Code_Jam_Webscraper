/*
 * omino.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Jason
 */

#include <iostream>
#include <fstream>

using namespace std;
// LETS PRECOMPUTE THIS BECAUSE IM TERRIBLE
bool terrible(int min, int max, int x) {
	if (min == 2 && max == 2) return (x>=3);
	if (min == 2 && max == 3) return (x>=4);
	if (min == 2 && max == 4) return (x>=3);
	if (min == 3 && max == 3) return (x>=4);
	if (min == 3 && max == 4) return false;
	if (min == 4 && max == 4) return false;
}

int main() {
	int c;
	ifstream cin;
	cin.open("input.txt");
	ofstream cout;
	cout.open("output.txt");
	cin >> c;
	for (int i = 1; i <= c; i++) {
		bool rich = false;
		int x, r, c;
		cin >> x >> r >> c;
		if (x>6) rich = true;
		else if (r*c % x != 0) rich = true;
		else if (x != 1 && x != 2) {
			int min = (r<c)?r:c, max = (r>c)?r:c;
			if (min == 1) rich = true;
			else rich = terrible(min, max, x);
		}
		cout << "Case #" << i << ": " << ((rich)?"RICHARD":"GABRIEL") << endl;
	}
}
