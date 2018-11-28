#include <iostream>
#include <fstream>
#include <array>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ifstream in ("A-small-attempt0.in");
	ofstream out ("magic_trick.out");
	int tests;
	in >> tests;
	int pos1, pos2;
	int square1[4][4];
	int square2[4][4];
	array<int,4> row_values; //different values in pos1
	array<int,4> new_rows; //array of new row numbers of pos1's values
	int answer;
	for (int a = 0; a < tests; ++a) {
		in >> pos1;
		pos1 -= 1;
		for (int b = 0; b < 4; ++b) {
			for (int c = 0; c < 4; ++c) {
				in >> square1[b][c];
			}
		}
		in >> pos2;
		pos2 -= 1;
		for (int d = 0; d < 4; ++d) {
			for (int e = 0; e < 4; ++e) {
				in >> square2[d][e];
			}
		}
		for (int z = 0; z < 4; ++z) {
            row_values[z] = square1[pos1][z]; //gets array of values at pos1
		}
		for (int f = 0; f < 4; ++f) {
			for (int g = 0; g < 4; ++g) {
				for (int h = 0; h < 4; ++h) {
					if (row_values[f] == square2[g][h]) { //runs through all values in pos1 and compares with each value in the square
						new_rows[f] = g; //puts the row value in new_rows
						continue;
					}
				}
			}
		}

		int count = 0; //gets reset for every test case
		int answer;
		for (int i = 0; i < 4; ++i) { //here we analyze the test cases
		    for (int j = 0; j < 4; ++ j) {
                if (square2[pos2][i] == row_values[j]) {
                    count += 1;
                    answer = row_values[j]; //doesn't matter if this gets overwritten because we only care if its value is set once
                }
		    }
		}
        if (count == 0) {
            if (a != tests-1) {
                out << "Case #" << a+1 << ": Volunteer cheated!\n";
            }
            else {
                out << "Case #" << a+1 << ": Volunteer cheated!" << endl;
            }
        }
        else if (count == 1) {
            if (a != tests-1) {
                out << "Case #" << a+1 << ": " << answer << '\n';
            }
            else {
                out << "Case #" << a+1 << ": " << answer << endl;
            }
        }
        else {
            if (a != tests-1) {
                out << "Case #" << a+1 << ": Bad magician!\n";
            }
            else {
                out << "Case #" << a+1 << ": Bad magician!" << endl;
            }
        }
    }
	return 0;
}
