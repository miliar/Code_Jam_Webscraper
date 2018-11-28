#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");


string solve() {

	int X, R, C;
	in >> X >> R >> C;
	if (X == 1)
		return "GABRIEL";
	if (X == 2) {
		if (R*C % 2 == 0)
			return "GABRIEL";
		else
			return "RICHARD";
	}
	if (X == 4) {
		if (R*C % 4 != 0)
			return "RICHARD";
		if (R*C <= 8)
			return "RICHARD";
		return "GABRIEL";
	}
	if (X == 3) {
		if (R*C % 3 != 0)
			return "RICHARD";
		if (R*C == 3)
			return "RICHARD";
		return "GABRIEL";
	}

}


int main() {



	int T;
	in >> T;

	for (int i = 1; i <= T; ++i) {
		out << "Case #" << i << ": " << solve() << "\n";
	}

	return 0;
}