//============================================================================
// Name        : GJam1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!\n" << endl; // prints !!!Hello World!!!


	std::fstream inFile, outFile;
	inFile.open ("test.txt", std::fstream::in);
	outFile.open ("result.txt", std::fstream::out);

	int tcCount =0 ;
	int sCount =0 ;
	char tempReadingDigit;
	int tempReading=0;

	//x = inFile.read();
	inFile >> tcCount;
	for (int i = 0; i < tcCount; i++) {
		inFile >> sCount;
		//cout << sCount<< std::endl;
		int counter =0;
		int requiredCounter =0;
		inFile.get(tempReadingDigit); // for the space
		for (int j = 0; j < sCount+1; j++) {
			//inFile >> noskipws >> tempReadingDigit;
			inFile.get(tempReadingDigit);
			tempReading = atoi(&tempReadingDigit);
			//cout << tempReading<< std::endl;
			if (counter >= j)
				counter+=tempReading;
			else {
				requiredCounter+=(j-counter);
				counter+=(tempReading + (j-counter));
			}

			//cout << counter<< std::endl;
			//cout << requiredCounter<< std::endl;
		}
		outFile << "Case #" <<i+1 << ": " << requiredCounter << std::endl;
	}

	//cout << x;
	//outFile << " more lorem ipsum";

	inFile.close();
	outFile.close();


	return 0;
}
