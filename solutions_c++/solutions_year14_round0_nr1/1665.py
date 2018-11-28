#include <iostream>
#include <cstdio>
using namespace std;

int frows[5][5];
int srows[5][5];

int main() {

		int testcase = 0;

		cin >> testcase;
		for (int tCase = 1; tCase <=testcase; ++tCase) {
				int fRow, sRow;

				cin >> fRow;
				for (int i=0; i<4; ++i) for (int j=0; j<4; ++j) 
						cin >> frows[i][j];
				cin >> sRow;
				for (int i=0; i<4; ++i) for (int j=0; j<4; ++j)
						cin >> srows[i][j];

				int numOfMatch = 0;
				int matchCard = 0;
				for (int i=0; i<4; ++i) for (int j=0; j<4; ++j) {
						if (frows[fRow-1][i] == srows[sRow-1][j]) {
								++numOfMatch;
								matchCard = frows[fRow-1][i];
						}
				}

				printf("Case #%d: ", tCase);
				if (numOfMatch == 1) {
						cout << matchCard << endl;
				}
				else if (numOfMatch > 1) {
						cout << "Bad magician!" << endl;
				}
				else {
						cout << "Volunteer cheated!" << endl;
				}
		}
}
