#include <iostream>
#include <vector>
#include <fstream>

//auto& in = std::cin;
//auto& out = std::cout;

std::string table[5][5][5];

int main() {
	std::ifstream in("D-small-attempt2.in");
	std::ofstream out("output.txt");

	table[4][2][2] = "RICHARD";
	table[4][1][4] = "RICHARD";
	table[4][4][1] = "RICHARD";
	table[4][2][4] = "RICHARD";
	table[4][4][2] = "RICHARD";
	table[4][4][4] = "GABRIEL";
	table[4][4][3] = "GABRIEL";
	table[4][3][4] = "GABRIEL";

	int t; in >> t;
	for (int k = 1; k <= t; ++k) {
		int x, r, c;
		in >> x >> r >> c;

		std::string winner;

		if (x == 1) {
			winner = "GABRIEL";
		} else if (x == 2) {
			if (r*c % 2 == 0)
				winner = "GABRIEL";
			else
				winner = "RICHARD";
		} else if (x == 3) {
			if ((r*c) % 3 == 0) {
				if (r == 1 || c == 1) {
					winner = "RICHARD";
				}
				else {
					winner = "GABRIEL";
				}
			} else {
				winner = "RICHARD";
			}
		} else if (x == 4) {
			if (std::max(r,c) == 3 || std::min(r,c) == 1)
				winner = "RICHARD";
			else if (r*c % 4 == 0)
				winner = table[x][r][c];
			else
				winner = "RICHARD";
		}

		out << "Case #" << k << ": " << winner << '\n';
	}

	return 0;
}