//Google Code Jam 2015 - Qualification
//Standing Ovation (Problem A)
//Matthew "sxmn" Zaneski, 4/11/2015
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream inFile;
	ofstream outFile;
	int numCases;

	inFile.open("A-small-attempt1.in");
	outFile.open("output.txt");

	inFile >> numCases;
	inFile.ignore(1, '\n');


	for (int t = 0; t < numCases; t++) {
		int sMax, sNum = 0, friends = 0;

		sMax = inFile.get() - '0';
		inFile.ignore(1, ' ');

		for (int sLevel = 0; sLevel <= sMax; sLevel++) {
			int sLevelNum = inFile.get() - '0';

			if (sLevelNum > 0) {
				if (sNum < sLevel) {
					friends += (sLevel - sNum);
					sNum += friends;
				}
			}

			sNum += sLevelNum;
		}

		inFile.ignore(1024, '\n');
		outFile << "Case #" << (t + 1) << ": " << friends << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}