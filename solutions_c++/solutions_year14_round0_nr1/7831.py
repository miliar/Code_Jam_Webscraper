#include <fstream>
#include <iostream>
#include <string>

using namespace std;



int main() {
	
	int numCases;
	
	const string bad = "Bad magician!";
	const string cheat = "Volunteer cheated!";
	
	string filename;
	cin >> filename;

	ifstream infile (filename);

	ofstream outfile ("output.txt");

	infile >> numCases;

	for (int aCase = 0; aCase < numCases; ++aCase) {
		int q1;
		int q2;
		int grid1[4][4];
		int grid2[4][4];		
		int dupCt = 0;
		int dup;
		
		
		infile >> q1;
		
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				infile >> grid1[i][j];
			}
		}

		infile >> q2;
		
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				infile >> grid2[i][j];
			}
		}
		
		--q1;
		--q2;
		
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (grid1[q1][i] == grid2[q2][j]) {
					dupCt++;
					dup = grid1[q1][i];
					if (dupCt > 1) {
						break;
					}
				}
			}
		}
		
		
		outfile << "Case #" << aCase + 1 << ": ";
		
		if (dupCt == 1) {
			outfile << dup;
		} else if (dupCt == 0) {
			outfile << cheat;
		} else {
			outfile << bad;
		}
		outfile << "\n";
	}
}