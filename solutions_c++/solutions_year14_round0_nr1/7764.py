#include <iostream>
#include <fstream>
using namespace std;
typedef unsigned char uchar;

int main(int argc, char** argv) {
	ifstream inputFile("A-small-attempt0.in");
	ofstream outputFile("a.out");

	if(inputFile.is_open() ) {
		unsigned int T;
		int choise1, choise2;
		int variants1[16], variants2[16];

		inputFile >> T;
		for(unsigned int i = 0; i < T; ++i) {
			inputFile >> choise1;
			for(uchar j = 0; j < 16; ++j)
				inputFile >> variants1[j];

			inputFile >> choise2;
			for(uchar j = 0; j < 16; ++j)
				inputFile >> variants2[j];

			int* line1 = variants1 + (choise1 - 1) * 4;
			int* line2 = variants2 + (choise2 - 1) * 4;
			
			int countElemtens = 0;
			int element = 0;

			for(uchar j1 = 0; j1 < 4; ++j1)
				for(uchar j2 = 0; j2 < 4; ++j2)
					if( *(line1 + j1) == *(line2 + j2) ) {
						++countElemtens;
						element = *(line1 + j1);
					}

			outputFile << "Case #" << i + 1 << ": ";
			if(countElemtens == 0)
				outputFile << "Volunteer cheated!";
			else if(countElemtens > 1)
				outputFile << "Bad magician!";
			else
				outputFile << element;
			outputFile << endl;
		}
	}

	inputFile.close();
	outputFile.close();
	return 0;
}
