#include <fstream>
#include <limits>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> names({"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"});
map<int, char> firstWave;
map<int, char> secondWave;

void removeChars(string &source, string chars) {
	for (auto it = chars.begin(); it != chars.end(); it++) {
		source.erase(source.find(*it), 1);
	}
}

string computeCase(istream &is) {
	vector<int> usedDigits;
	string result;
	string raw;
	is >> raw;
	for (auto it = firstWave.begin(); it != firstWave.end(); it++) {
		while (raw.find(it->second) != string::npos) {
			usedDigits.push_back(it->first);
			removeChars(raw, names[it->first]);
		}
	}
	for (auto it = secondWave.begin(); it != secondWave.end(); it++) {
		while (raw.find(it->second) != string::npos) {
			usedDigits.push_back(it->first);
			removeChars(raw, names[it->first]);
		}
	}
	for (unsigned long i = 0; i < raw.length() / 4; i++) {
		usedDigits.push_back(9);
	}
	sort(usedDigits.begin(), usedDigits.end());
	for (auto it = usedDigits.begin(); it != usedDigits.end(); it++) {
		result.append(to_string(*it));
	}
	return result;
}

int main() {

	firstWave[0] = 'Z';
	firstWave[2] = 'W';
	firstWave[4] = 'U';
	firstWave[6] = 'X';
	firstWave[8] = 'G';

	secondWave[1] = 'O';
	secondWave[3] = 'R';
	secondWave[5] = 'F';
	secondWave[7] = 'S';

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
