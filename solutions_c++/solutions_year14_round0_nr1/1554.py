#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <windows.h>

using namespace std;

void processCase(ifstream &infile, ofstream &outfile, int number);

int main() {
	ifstream infile;
	ofstream outfile;
	string filename = "A-small-attempt0.in";
	string filename1 = "A-small-practice.out";
	infile.open(filename.c_str());
	outfile.open(filename1.c_str());
	int cases;
	infile >> cases;
	for (int i = 1; i <= cases; i++) {
		processCase(infile, outfile, i);
	}
	return 0;
}

void processCase(ifstream &infile, ofstream &outfile, int number) {
	outfile << "Case #" << number << ": ";
	int r1, r2;
	int m1[4][4];
	int m2[4][4];
	infile >> r1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			infile >> m1[i][j];
		}
	}
	infile >> r2;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			infile >> m2[i][j];
		}
	}
	int arr[17];
	for (int i = 0; i < 17; i++) {
		arr[i] = 0;
	}
	bool hasCommon = false;
	int common;
	for (int i = 0; i < 4; i++) {
		arr[m1[r1 - 1][i]] = 1;
	}
	for (int i = 0; i < 4; i++) {
		int index = m2[r2 - 1][i];
		if (arr[index] == 1) {
			if (hasCommon) {
				outfile << "Bad magician!" << endl;
				return;
			} else {
				common = index;
				hasCommon = true;
			}
		}
	}
	if (hasCommon) {
		outfile << common << endl;
	} else {
		outfile << "Volunteer cheated!" << endl;
	}
	//outfile << "Case #" << number << ": " << total << endl;
}