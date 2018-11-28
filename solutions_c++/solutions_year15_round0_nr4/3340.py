#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

int main() {
	ifstream in("D-small-0.in");
	ofstream out("D-small-0.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		string r;
		int X, R, C; in >> X >> R >> C;
		if ((R * C) % X != 0) r = "RICHARD";
		else if (X == 1 || X == 2) r = "GABRIEL";
		else if (X == 3) {
			if (R == 1 || C == 1) r = "RICHARD";
			else r = "GABRIEL";
		}
		else if (X == 4) {
			if (R == 1 || C == 1) r = "RICHARD";
			else if (R == 2 || C == 2) r = "RICHARD";
			else r = "GABRIEL";
		}
		out << "Case #" << x << ": " << r << endl;
	}

	return 0;
}
