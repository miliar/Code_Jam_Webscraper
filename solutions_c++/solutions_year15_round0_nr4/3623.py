//Google Code Jam 2015 - Qualification
//Ominous Omino (Problem D)
//Matthew "sxmn" Zaneski, 4/11/2015
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

enum Winner { RICHARD, GABRIEL };

int main(){
	ifstream inFile;
	ofstream outFile;
	string fileName;
	int numCases;
	Winner winner;

	cout << "input file: ";
	getline(cin, fileName);

	inFile.open(fileName.c_str());
	outFile.open("output.txt");

	inFile >> numCases;

	for (int t = 0; t < numCases; t++) {
		int x, r, c, product;

		inFile >> x >> r >> c;

		product = r * c;

		switch (x) {
		case 1:
			winner = GABRIEL;
			break;
		case 2:
			if (product % x == 0)
				winner = GABRIEL;
			else
				winner = RICHARD;
			break;
		case 3:
			if ((product % x == 0) &&
				((r >= 3 && c >= 2) || (r >= 2 && c >= 3)))
				winner = GABRIEL;
			else
				winner = RICHARD;
			break;
		case 4:
			if ((product % x == 0) &&
				((r >= 4 && c >= 3) || (r >= 3 && c >= 4)))
				winner = GABRIEL;
			else
				winner = RICHARD;
			break;
		case 5:
			if ((product % x == 0) &&
				((r >= 5 && c >= 3) || (r >= 3 && c >= 5)))
				winner = GABRIEL;
			else
				winner = RICHARD;
			break;
		case 6:
			if ((product % x == 0) &&
				((r >= 6 && c >= 3) || (r >= 3 && c >= 6)))
				winner = GABRIEL;
			else
				winner = RICHARD;
			break;
		default:
			winner = RICHARD;
		}

		switch (winner) {
			case RICHARD:
				outFile << "Case #" << (t + 1) << ": " << "RICHARD" << endl;
				break;
			case GABRIEL:
				outFile << "Case #" << (t + 1) << ": " << "GABRIEL" << endl;
				break;
		}
		
	}

	inFile.close();
	outFile.close();
	return 0;
}