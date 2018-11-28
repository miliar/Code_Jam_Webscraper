#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

int main() {
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("A-small-attempt1.out");
	unsigned int nCases;
	infile >> nCases;
	double arrange[4][4];
	for (unsigned int i = 0; i < nCases; i++) {
		int rowindex;
		infile >> rowindex;
		for (unsigned int j = 0; j < 4; j++) {
			for (unsigned int k = 0; k < 4; k++) {
				infile >> arrange[j][k];
			}
		}
		double row1[4];
		for (unsigned int j = 0; j < 4; j++)
			row1[j] = arrange[rowindex - 1][j];
		infile >> rowindex;
		for (unsigned int j = 0; j < 4; j++) {
			for (unsigned int k = 0; k < 4; k++) {
				infile >> arrange[j][k];
			}
		}
		double row2[4];
		for (unsigned int j = 0; j < 4; j++)
			row2[j] = arrange[rowindex - 1][j];
		// compare row1 and row2
		int nCommon = 0;
		int commonindex;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (row1[j] == row2[k]) {
					commonindex = j;
					++nCommon;
					continue;
				}
			}
		}
		outfile << "Case #" << (i + 1) << ": ";
		if (nCommon == 1) {
			outfile << row1[commonindex] << endl;
		}
		else if (nCommon >= 2) {
			outfile << "Bad magician!" << endl;
		}
		else {
			outfile << "Volunteer cheated!" << endl;
		}
	}
	infile.close();
	outfile.close();
}

 