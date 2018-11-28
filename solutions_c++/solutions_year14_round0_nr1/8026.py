#include<fstream>
#include<iostream>
#include<string>

int main()
{
	std::ifstream fin("A-small-attempt0.in");
	std::ofstream fout("A-small-attempt0.out");

	int cases, card = 0, rowNum1, rowNum2, row1[4], row2[4], cards1[4][4], cards2[4][4], numMatches = 0;

	fin >> cases;

	for(int test = 1; test <= cases; ++test) {

		fin >> rowNum1;

		for(int i = 0; i < 4; ++i) {
			for(int k = 0; k < 4; ++k) {
				fin >> cards1[i][k];
			}
		}

		fin >> rowNum2;

		for(int i = 0; i < 4; ++i) {
			for(int k = 0; k < 4; ++k) {
				fin >> cards2[i][k];
			}
		}

		for(int i = 0; i < 4; ++i) {
			for(int k = 0; k < 4; ++k) {
				if(cards1[rowNum1 - 1][i] == cards2[rowNum2 - 1][k]) {
					card = cards1[rowNum1 - 1][i];
					++numMatches;
				}
			}
		}


		fout << "Case #" << test << ": ";
		if(numMatches == 1) {
			fout << card;
		} else if(numMatches > 1) {
			fout << "Bad magician!";
		} else {
			fout << "Volunteer cheated!";
		}

		fout << '\n';

		numMatches = 0;
	}

	return 0;
}
