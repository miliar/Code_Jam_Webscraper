#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int T;
	input >> T;
	for (int i = 0; i < T; ++i) {
		int X, R, C;
		input >> X >> R >> C;
		bool solvable = true;
		if ((R*C) % X || X >= 7) {
			solvable = false;
		}
		if (R < 1 + (X - 1) / 2 || C < 1 + (X - 1) / 2) { // _| shape
			solvable = false;
		}
		if (X > R && X > C) { // X by 1
			solvable = false; 
		}
		if (X == 4 && (R == 2 || C == 2)) { // .:.
			solvable = false;
		}
		if (X == 6 && (R == 3 || C == 3)) { // .|..
			solvable = false;
		}
		output << "Case #" << (i + 1) << ": " << (solvable ? "GABRIEL" : "RICHARD") << endl;
	}
	return 0;
}