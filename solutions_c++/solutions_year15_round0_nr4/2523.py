#include <fstream>
#include <string>

bool case2 (int R, int C) {
	return R*C % 2;
}

bool case3 (int  R, int C) {
	if (R*C % 3)
		return true;

	if (R == 1 || C == 1)
		return true;

	return false;
}

bool case4 (int R, int C) {
	if (R*C % 4)
		return true;

	if (R <= 2 || C <= 2)
		return true;

	if (R < 4 && C < 4)
		return true;

	return false;
}

bool richardWins(int X, int R, int C) {
	switch (X) {
		case 1:
			return false;
		case 2:
			return case2(R,C);
		case 3:
			return case3(R,C);
		case 4:
			return case4(R,C);
	}
}


int main (int argc, char** argv) {
	std::ifstream in (argv[1]);
	std::ofstream out ("Omino.out");

	int cases;
	in >> cases;

	for (int i = 1; i <= cases; ++i) {
		int X, R, C;
		in >> X >> R >> C;
		std::string res = richardWins(X,R,C) ? "RICHARD" : "GABRIEL";
		out << "Case #" << i << ": " << res << "\n";
	}
}
