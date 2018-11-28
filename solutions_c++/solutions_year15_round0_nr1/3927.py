// basic file operations
#include <iostream>
#include <fstream>
using namespace std;

int charToInt (char c) {
	if (c == '0')
		return 0;
	if (c == '1')
		return 1;
	if (c == '2')
		return 2;
	if (c == '3')
		return 3;
	if (c == '4')
		return 4;
	if (c == '5')
		return 5;
	if (c == '6')
		return 6;
	if (c == '7')
		return 7;
	if (c == '8')
		return 8;
	if (c == '9')
		return 9;
}

int main () {
	int t; // Number of test cases
	int sMax;
	char shyness[2001];
	int finalRs;
	int tempCount;

	char *inname = "inputA.txt";
	ifstream infile(inname);

	ofstream outputFile;
	outputFile.open ("outputA.txt");

	infile >> t;
	
	for (int z = 0; z < t; z++) { 
		infile >> sMax;
		infile >> shyness;
		finalRs = 0;
		tempCount = charToInt(shyness[0]);
		for (int i = 1; i <= sMax; i++) {
			if (i > tempCount && charToInt(shyness[i]) > 0) { 
				finalRs += (i - tempCount);
				tempCount += (i - tempCount);
			}
			tempCount += charToInt(shyness[i]);
			if (z == 2)
			cout << finalRs << " " << tempCount << "\n";
		}
		outputFile << "Case #" << (z+1) << ": " << finalRs << "\n";
	} 
	infile.close();
	outputFile.close();
	return 0;
}