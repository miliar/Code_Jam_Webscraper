#include <iostream>
#include <fstream>
#include <vector>
#include "CGCJLib.hpp"

#define PROBLEM_LETTER "C"
#define SIZE "small"
#define VERSION_NUM "5"

using namespace std;

vector<int> quaternionString, foundI, foundK;
vector<bool> isFoundINegative, isFoundKNegative;
int quaternionStringRepetition, quaternionStringSize;

// 1 -> 1
// i -> 2
// j -> 3
// k -> 4
inline int letterToQuaternionSymbol(char c) {
	return c - 'g';
}

// ignores negatives
inline char quaterinionSymbolToLetter(int i) {
	return 'g' + i;
}

const int quaternionTable[4][4] = {{ 1, 2, 3, 4 }, { 2, -1, 4, -3 }, { 3, -4, -1, 2 }, { 4, 3, -2, -1 }};

inline int resolveQuaternionMultiplication(int a, int b) {
	return (quaternionTable[abs(a)-1][abs(b)-1] * ((a < 0) ^ (b < 0) ? -1 : 1));
}

void seekI() {
	int previousQuaternion = quaternionString.at(0);
	if(previousQuaternion == 2) {
		foundI.push_back(0);
		isFoundINegative.push_back(false);
	}
	int currentQuaternion;
	for(int i=1;i<quaternionStringSize * quaternionStringRepetition - 2;i++) {
		//cout << previousQuaternion << " ";
		currentQuaternion = quaternionString.at(i % quaternionStringSize); // <- could remove mod by breaking up loop
		previousQuaternion = resolveQuaternionMultiplication(previousQuaternion, currentQuaternion);
		if(abs(previousQuaternion) == 2) {
			foundI.push_back(i);
			isFoundINegative.push_back(previousQuaternion < 0);
		}
	}
	//cout << endl;
}

void seekK() {
	int previousQuaternion = quaternionString.at((quaternionStringSize * quaternionStringRepetition - 1) % quaternionStringSize);
	if(previousQuaternion == 4) {
		foundK.push_back(quaternionStringSize * quaternionStringRepetition - 1);
		isFoundKNegative.push_back(false);
	}
	int currentQuaternion;
	for(int i=quaternionStringSize * quaternionStringRepetition - 2;i>1;i--) {
		currentQuaternion = quaternionString.at(i % quaternionStringSize); // <- could remove mod by breaking up loop
		previousQuaternion = resolveQuaternionMultiplication(currentQuaternion, previousQuaternion);
		if(abs(previousQuaternion) == 4) {
			foundK.push_back(i);
			isFoundKNegative.push_back(previousQuaternion < 0);
		}
	}
}

bool doesJFit(int startIndex, bool isINegative) {
	int previousQuaternion = quaternionString.at(startIndex % quaternionStringSize);
	int currentK = foundK.size()-1;
	while(currentK >= 0 && foundK.at(currentK) <= startIndex) currentK--;
	if(currentK < 0) return false;
	if(previousQuaternion == 3 && foundK.at(currentK) == startIndex+1 && isFoundKNegative.at(currentK) == isINegative) {
		return true;
	}
	int currentQuaternion;
	for(int i=startIndex+1;i<foundK.at(0);i++) {
		currentQuaternion = quaternionString.at(i % quaternionStringSize); // <- could remove mod by breaking up loop
		previousQuaternion = resolveQuaternionMultiplication(previousQuaternion, currentQuaternion);
		while(foundK.at(currentK) <= i) currentK--;
		if(currentK < 0) return false;
		if(abs(previousQuaternion) == 3 && foundK.at(currentK) == i+1 && (isINegative + isFoundKNegative.at(currentK) + (previousQuaternion < 0)) % 2 == 0) {
			return true;
		}
	}
	return false;
}

int main() {
	ifstream input(CGCJLib::getSourcePath() + "/" + PROBLEM_LETTER + "-" + SIZE + "-" + VERSION_NUM + ".in");
	ofstream output(CGCJLib::getSourcePath() + "/" + PROBLEM_LETTER  + "-" + SIZE + "-" + VERSION_NUM + ".out");
	output.setf(ios::fixed, ios::floatfield);
	output.precision(7);
	int testCases;
	input >> testCases;
	for(int i=0;i<testCases;i++) {
		//cout << i << endl;
		input >> quaternionStringSize >> quaternionStringRepetition;
		quaternionString.clear();
		foundI.clear();
		isFoundINegative.clear();
		foundK.clear();
		isFoundKNegative.clear();
		input.get();
		for(int j=0;j<quaternionStringSize;j++) {
			quaternionString.push_back(letterToQuaternionSymbol(input.get()));
		}
		if(quaternionStringSize * quaternionStringRepetition < 3) {
			output << "Case #" << i+1 << ": NO" << endl;
			//cout << quaternionStringSize << " " << quaternionStringRepetition << endl;
			goto testCaseEnd;
		}
		if(quaternionStringSize * quaternionStringRepetition == 3) {
			if(quaternionString.at(0) == 2 && quaternionString.at(1) == 3 && quaternionString.at(2) == 4) {
				output << "Case #" << i+1 << ": YES" << endl;
			}
			else {
				output << "Case #" << i+1 << ": NO" << endl;
			}
			goto testCaseEnd;
		}
		seekI();
		if(foundI.empty()) {
			output << "Case #" << i+1 << ": NO" << endl;
			goto testCaseEnd;
		}
		seekK();
		if(foundK.empty()) {
			output << "Case #" << i+1 << ": NO" << endl;
			goto testCaseEnd;
		}
		for(int j=0;j<foundI.size();j++) {
			if(doesJFit(foundI.at(j)+1, isFoundINegative.at(j))) {
				output << "Case #" << i+1 << ": YES" << endl;
				goto testCaseEnd;
			}
		}
		output << "Case #" << i+1 << ": NO" << endl;
		// A quote from Dijkstra seems fitting here: "the quality of programmers is a decreasing function of the density of goto statements in the programs they produce"
		testCaseEnd:;
	}
	return 0;
}
