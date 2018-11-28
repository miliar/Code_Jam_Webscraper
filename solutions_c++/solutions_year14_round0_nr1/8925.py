#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;


const string PATH = "C:/ws/vs_projects/GoogleCodeJam2014/Files/";
const string FILENAME = "A-small-attempt0";



int main() {
	ifstream fin(PATH + FILENAME + ".in");
	ofstream out(PATH + FILENAME + ".out");

	int T, i, j, row1, row2;
	fin >> T;
	int board1[4][4], board2[4][4], found;
	int t = T;
	bool multiple, consistent;
	while (--t >= 0) {		
		fin >> row1;
		row1--;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				fin >> board1[i][j];
			}
		}

		fin >> row2;
		row2--;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				fin >> board2[i][j];
			}
		}

		// check multiple cards
		// check if volunteer is consistent
		multiple = false;
		consistent = false;
		for (i = 0; i < 4 && !multiple; i++) {
			for (j = 0; j < 4 && !multiple; j++) {
				if (board1[row1][i] == board2[row2][j]) {
					if (consistent) {
						multiple = true;
					}
					consistent = true;
					found = board1[row1][i];
					break;
				}
			}			
		}


		// Output:
		out << "Case #" << (T - t) << ": ";
		if (multiple) {
			out << "Bad magician!";
		} 
		else if (!consistent) {
			out << "Volunteer cheated!";
		} 
		else {
			out << found;
		}
		out << "\n";
	}
	return 0;
}