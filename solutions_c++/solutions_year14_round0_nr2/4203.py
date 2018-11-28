//============================================================================
// Name        : cookie_clicker.cpp
// Author      : Vasilis Pardalis
// Version     :
// Copyright   :
//============================================================================

#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <cstdio>

using namespace std;


void errmsg(const char *msg) {

	cout << msg << endl;
	exit(EXIT_FAILURE);
}


int main() {


	int iCases;

	cin >> iCases;
	if (iCases > 0) {
		for (int i = 0; i < iCases; i++) {
			int iSteps = 0;
			double fC, fX, fF, fTotal = 0.0;
			double fTe, fTf;

			cin >> fC >> fF >> fX;


			while (true) {
				fTe = fX / (2.0 + (fF * iSteps));
				fTf = fC / (2.0 + (fF * iSteps));

				if (fTf < fTe) {

					double fTmp = fX / (2.0 + (fF * (iSteps + 1)));
					if ((fTf + fTmp) < fTe) {
						fTotal += fTf;
						iSteps++;
					}
					else {
						fTotal += fTe;
						break;
					}

				}
				else {
					fTotal += fTe;
					break;
				}

			}


			cout << "Case #" << (i + 1) << ": " << fixed << setprecision(7) << showpoint << fTotal << endl;

		}


	}
	else errmsg("No test cases defined!");

	return 0;
}
