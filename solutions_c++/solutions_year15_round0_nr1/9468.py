#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std; 

int main() {
	size_t numTestCases; 
	char *inname = "C:/A-large.in";
	ifstream infile(inname);
	std::ofstream outfile("A-large-result.txt", std::ofstream::out);

	if (!infile) {
		cout << "There was a problem opening the file!" << endl;
	}

	infile >> numTestCases;

	for (size_t test = 1; test <= numTestCases; ++test) {
		size_t maxShyness; 
		string shynessString; 
		infile >> maxShyness >> shynessString;
		size_t runningTotal = shynessString[0] -'0';
		size_t addedPeople = 0;
		for (size_t shynessIndex = 1; shynessIndex <= maxShyness; shynessIndex++) {
			size_t currentShyness = shynessString[shynessIndex] - '0'; 
			if (currentShyness != 0) {
				if (runningTotal < shynessIndex) {
					size_t difference = shynessIndex - runningTotal; 
					addedPeople += difference;
					runningTotal += difference;
				}
				runningTotal += currentShyness;
			}
		}
		outfile << "Case #" << test << ": " << addedPeople << endl;
	}

	infile.close();
	outfile.close();

   	return 0;
}