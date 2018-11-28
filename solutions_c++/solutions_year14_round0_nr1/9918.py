//============================================================================
// Name        : gcj14.cpp
// Author      : Ravi
// Version     :
// Copyright   : what copyright notice?
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;

#define INPUT "/home/ravi/workspace/gcj14/inp/A-small-attempt1.in"

void proba(char *inpfile) {
	ifstream input(inpfile);
	ofstream output("output.txt");

	string temp;
	// Number of test cases
	getline (input, temp);
	int testcases = atoi(temp.c_str());

	int count = 1;
	string line;
	int firstrow, secondrow;
	int firstdraw[4][4], seconddraw[4][4];
	while(input.good()) {
		cout << count;
		if (count > testcases)
			break;

		getline (input, line);
		stringstream stream(line);

		stream >> firstrow;
		for (int i = 0; i < 4; i++) {
			getline (input, line);
			stringstream stream(line);
			for (int j = 0; j < 4 ; j++) {
				stream >> firstdraw[i][j];
			}
		}

		getline (input, line);
		stringstream stream1(line);
		stream1 >> secondrow;
		for (int i = 0; i < 4; i++) {
			getline (input, line);
			stringstream stream(line);
			for (int j = 0; j < 4 ; j++) {
				stream >> seconddraw[i][j];
			}
		}

		int nummatches = 0, lastidxmatch = 0;
		for (int i = 0; i < 4; i++) {
			int elem = firstdraw[firstrow-1][i];
			for (int j = 0; j < 4; j++) {
				if (elem == seconddraw[secondrow-1][j]) {
					lastidxmatch = i;
					nummatches++;
				}
			}
		}

		output << "Case #" << count << ": ";
		if (nummatches == 1) {
			output << firstdraw[firstrow-1][lastidxmatch] << endl;
		} else if (nummatches > 1) {
			output << "Bad magician!" << endl;
		} else if (nummatches == 0) {
			output << "Volunteer cheated!" << endl;
		}
		count++;
	}
}

int main() {
	proba(INPUT);
	cout << "Junk fellow" << endl; // prints Junk fellow
	return 0;
}
