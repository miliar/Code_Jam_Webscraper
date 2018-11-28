
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
	int T = 0;
	string fileName = "output.txt";
	fstream fileOut(fileName.c_str());
	fstream fileIn(argv[1]);

	fileIn >> T;
	string input;
	int solutions[T];
	int sMax; 
		
	for(int i = 0; i < T; i++) {
		fileIn >> sMax;
		fileIn >> input;
	
		solutions[i] = 0;
		int tSum = 0;
		char cI;
		int I;	
		for(int j = 0; j <= sMax; j++) {
			cI = input[j];
			I = cI - '0';

			if(I == 0) continue;

			if(j <= tSum) {
				tSum += I;
			} else {
				solutions[i] += j - tSum;
				tSum += j - tSum;
				tSum += I;
			}
		}
	}

	for(int i = 0; i < T; i++) {
		fileOut << "Case #" << i+1 << ": " << solutions[i] << endl;
	}
}


