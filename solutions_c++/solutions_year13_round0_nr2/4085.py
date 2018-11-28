//============================================================================
// Name        : LawnMower.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
	ifstream infile;
	infile.open(argv[1]);
	int ncases;
	infile >> ncases;
	for (int i=0; i<ncases; ++i) {
		int rows, columns;
		infile >> rows;
		infile >> columns;
		int* pattern = new int[rows*columns];
		int* rowmax = new int[rows];
		int* colmax = new int[columns];

		for (int j=0; j<rows; ++j) {
			for (int k=0; k<columns; ++k) {
				infile >> pattern[j*columns + k];
			}
		}

		for (int j=0; j<rows; ++j) {
			for (int k=0; k<columns; ++k) {
				if (rowmax[j] < pattern[j*columns + k]) {
					rowmax[j] = pattern[j*columns + k];
				}
			}
			//cout << rowmax[j] << " " << j << endl;
		}
		//cout << endl;
		for (int j=0; j<columns; ++j) {
			for (int k=0; k<rows; ++k) {
				if (colmax[j] < pattern[k*columns + j]) {
					colmax[j] = pattern[k*columns + j];
				}
			}
			//cout << colmax[j] << " " << j << endl;
		}

		bool broken;
		for (int j=0; j<rows; ++j) {
			for (int k=0; k<columns; ++k) {
				if ((pattern[j*columns + k] < rowmax[j]) &&
					(pattern[j*columns + k] < colmax[k])) {
					broken = true;
					break;
				}
			}
			if (broken) {
				break;
			}
		}
		if (broken) {
			cout << "Case #" << i+1 << ": NO" << endl;
			broken = false;
		}
		else {
			cout << "Case #" << i+1 << ": YES" << endl;
		}
	}
}
