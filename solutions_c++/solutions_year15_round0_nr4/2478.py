#include <iostream>
#include <fstream>

using namespace std;

int solve(istream& in) {
	int X, R, C;
	in >> X >> R >> C;

	if (R < X && C < X)
		return 1;
	int total = R * C;
	if (total % X != 0)
		return 1;

	switch (X) {
	case 1:
	case 2:
		return 0;
	case 3:
	case 4:
	case 5:
		if (R <= X-2 || C <= X-2)
			return 1;
		else
			return 0;
	case 6:
		if (R <= X-1 || C <= X-1)
			return 1;
		else 
			return 0;
	default: 
		return 1;
	}
}

int main() {

	ifstream fin("D-small-attempt2.in");
	ofstream fout("D-small-attempt2.out");
	int T;

	fin >> T;

	for (int i = 1; i <= T; i++) {
		fout << "Case #" << i << ": ";
		if (solve(fin))
			fout << "RICHARD";
		else
			fout << "GABRIEL";
		fout << endl;
	}

	fin.close();
	fout.close();

	return 0;
}
