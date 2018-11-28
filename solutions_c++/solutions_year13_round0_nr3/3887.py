#include <string>
#include <cmath>
#include "FairandSquare.h"

using namespace std;

FairandSquare::FairandSquare() {
	lower = 0;
	upper = 0;
	numFairandSquare = 0;
}

FairandSquare::FairandSquare(char* inputFile, char* outputFile) {
	ifstream fileIn(inputFile);
	string line;
	if (fileIn.fail()) {
		throw FairandSquareException("File cannot be read.");
	}
	getline(fileIn, line);
	numCases = stol(line);
	
	ofstream fileOut(outputFile);
	if (fileOut.fail()) {
		throw FairandSquareException("File cannot be written.");
	}
	long i;
	for (i=0; i<numCases; i++) {
		getline(fileIn, line, ' ');
		lower = stol(line);
		getline(fileIn, line);
		upper = stol(line);
		findFairandSquare(lower, upper);
		writeLine(fileOut, i);
	}
	fileOut.close();
}

void FairandSquare::findFairandSquare(long start, long end) {
	long j;
	long currentSqrt;
	numFairandSquare = 0;
	for (j=start; j<=end; j++) {
		if (isFair(j) && isSquare(j, currentSqrt) && isFair(currentSqrt)) {
			numFairandSquare++;
		}
	}
}

bool FairandSquare::isFair(long num) {
	string strRep = to_string(num);
	int k;
	int len = strRep.length();
	for (k=0; k<len/2; k++) {
		if (strRep[k] != strRep[len-k-1]) {
			return false;
		}
	}
	return true;
}

bool FairandSquare::isSquare(long num, long& currentSqrt) {
	long nominalSqrt = (long) sqrt((double)num);
	long k;
	for (k=nominalSqrt-1; k<=nominalSqrt+2; k++) {
		if (k * k == num) {
			currentSqrt = k;
			return true;
		}
	}
	currentSqrt = nominalSqrt; // shouldn't be used anyway
	return false;	
}

void FairandSquare::writeLine(ofstream& fileOut, long lineNum) const {
	fileOut << "Case #" << lineNum+1 << ": " << numFairandSquare << endl;
}
