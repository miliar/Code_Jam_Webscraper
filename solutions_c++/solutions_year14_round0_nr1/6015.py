// magic-trick.cpp: Jagermeister
// Description: GCJ Qualification Round 2014 - A

#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int T, F, S, C;

	std::ifstream input("C:\\Users\\mmatarazzo\\Downloads\\A-small-attempt0.in");
	std::ofstream output("C:\\Users\\mmatarazzo\\Downloads\\A-small-attempt0.out");

	input >> T;

	for (int i = 0; i < T; i++) {
		int first_row[4];
		int second_row[4];
		int count = 0;
		int match = 0;

		input >> F;

		if (F == 1) {
			for (int j = 0; j < 4; j++) {
				input >> first_row[j];
			}
			for (int j = 0; j < 12; j++) {
				input >> C;
			}
		} else if (F == 2) {
			for (int j = 0; j < 4; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> first_row[j];
			}
			for (int j = 0; j < 8; j++) {
				input >> C;
			}
		} else if (F == 3) {
			for (int j = 0; j < 8; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> first_row[j];
			}
			for (int j = 0; j < 4; j++) {
				input >> C;
			}
		} else if (F == 4) {
			for (int j = 0; j < 12; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> first_row[j];
			}
		}

		input >> S;

		if (S == 1) {
			for (int j = 0; j < 4; j++) {
				input >> second_row[j];
			}
			for (int j = 0; j < 12; j++) {
				input >> C;
			}
		} else if (S == 2) {
			for (int j = 0; j < 4; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> second_row[j];
			}
			for (int j = 0; j < 8; j++) {
				input >> C;
			}
		} else if (S == 3) {
			for (int j = 0; j < 8; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> second_row[j];
			}
			for (int j = 0; j < 4; j++) {
				input >> C;
			}
		} else if (S == 4) {
			for (int j = 0; j < 12; j++) {
				input >> C;
			}
			for (int j = 0; j < 4; j++) {
				input >> second_row[j];
			}
		}

		for (int j = 0 ; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (second_row[k] == first_row[j]) {
					count++;
					match = second_row[k];
				}
			}
		}

		if (count == 1) output << "Case #" << i+1 << ": " << match << endl;
		else if (count > 1) output << "Case #" << i+1 << ": Bad magician!" << endl;
		else if (count == 0) output << "Case #" << i+1 << ": Volunteer cheated!" << endl;

	}

	input.close();
	output.close();

	return 0;
}