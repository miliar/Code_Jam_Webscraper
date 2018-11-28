//============================================================================
// Name        : CodeJam14.cpp
// Author      : tbrknt
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

std::ifstream infile("A-small-attempt1.in");

int main() {
	int numbers[17], rows[2], noOfCases, x;
	infile >> noOfCases;

	for (int i = 0; i < noOfCases; i++) {
		std::fill_n(numbers, 17, 0);
		for (int j = 0; j < 2; j++) {
			infile >> rows[j];
			for (int k = 0; k < 4; k++) {
				int l;
				if (k + 1 == rows[j]) {
					for (l = 0; l < 4; l++) {
						infile >> x;
						numbers[x]++;
					}
				} else {
					infile >> l >> l >> l >> l;
				}

			}
		}
		int count = 0, answer = 0;
		for (int j = 1; j < 17; j++) {
			if (numbers[j] == 2) {
				count++;
				answer = j;
			}
		}

		cout << "Case #" << (i + 1) << ": ";

		if (count > 1) {	//more than 1 common
			cout << "Bad magician!";
		} else if (count < 1) {	// no common
			cout << "Volunteer cheated!";
		} else {	//1 common
			cout << answer;
		}

		cout << endl;
	}

	return 0;
}
