//============================================================================
// Name        : magic_trick.cpp
// Author      : Vasilis Pardalis
// Version     :
// Copyright   : 
//============================================================================

#include <iostream>
#include <stdlib.h>
#include <cstdio>

using namespace std;


void errmsg(const char *msg) {

	cout << msg << endl;
	exit(EXIT_FAILURE);
}


int main() {


	int iCases, iFirst, iSecond, iFound, iNum;
	int arrFirst[4][4];
	int arrSecond[4][4];

	cin >> iCases;
	if (iCases > 0) {
		for (int i = 0; i < iCases; i++) {
			iFound = 0;
			cin >> iFirst;
			for (int j = 0; j < 4; j++) cin >> arrFirst[j][0] >> arrFirst[j][1] >> arrFirst[j][2] >> arrFirst[j][3];
			cin >> iSecond;
			for (int j = 0; j < 4; j++) cin >> arrSecond[j][0] >> arrSecond[j][1] >> arrSecond[j][2] >> arrSecond[j][3];

			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					if (arrFirst[iFirst - 1][j] == arrSecond[iSecond - 1][k]) {iFound++; iNum = arrFirst[iFirst - 1][j];}
				}
			}

			cout << "Case #" << (i + 1) << ": ";

			if (iFound == 1) {
				cout << iNum << endl;
			}
			else if (iFound > 1) cout << "Bad magician!" << endl;
			else cout << "Volunteer cheated!" << endl;

		}


	}
	else errmsg("No test cases defined!");

	return 0;
}
