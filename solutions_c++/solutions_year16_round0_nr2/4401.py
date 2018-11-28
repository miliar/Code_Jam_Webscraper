#include <fstream>
#include <limits>
#include <string>
// #include <iostream>

using namespace std;

int getLastBS(string str) {
	for (auto it = str.rbegin(); it != str.rend(); it++) {
		if (*it == '-') {
			return str.rend() - it - 1;
		}
	}
	return -1;
}

void flip(string &str, int count) {
	for (auto it = str.begin(); it - str.begin() < count + 1; it++) {
		*it = *it == '+' ? '-' : '+';
	}
}

int computeCase(istream &is) {
	int flipCounts = 0;
	int lastBS;
	string pancakeString;
	is >> pancakeString;
	while ((lastBS = getLastBS(pancakeString)) != -1) {
		flipCounts++;
		flip(pancakeString, lastBS);
	}
	return flipCounts;
}

int main() {

	ifstream inF("in");
	fstream outF("out", fstream::out);
	int caseCount;
	inF >> caseCount;
	inF.ignore(numeric_limits<streamsize>::max(), '\n');
	for (int caseNum = 1; caseNum <= caseCount; caseNum++) {
		outF << "Case #" << caseNum << ": " << computeCase(inF) << endl;
	}
	return 0;

}
