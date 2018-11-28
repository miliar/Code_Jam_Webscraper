#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {

	int testCases = 0;

	fstream inputFile;
	fstream outputFile;

  	inputFile.open ("A-large.in", std::ios::in);
	outputFile.open("A-large.out", std::ios::out);

	inputFile >> testCases;
	
	for (int i = 0 ; i < testCases; i++) {

			int sMax;
			string shynesses;
			inputFile >> sMax >> shynesses;
			vector<int> shyVector;
		
			for (int j = 0; j <= sMax; j++) {
				shyVector.push_back(shynesses.at(j) - '0');
			}
			
			int standingAudience = 0;
			int extraFriends = 0; 
			
			for (int j = 0; j <= sMax; j++) {
				if( j > standingAudience) {
					extraFriends += j - standingAudience;
					standingAudience += j - standingAudience;
				}
				standingAudience += shyVector.at(j);
			}
					
			outputFile << "Case #" << i + 1 << ": " << extraFriends << endl;
	}

	inputFile.close();
	outputFile.close();

	return 0;
}
