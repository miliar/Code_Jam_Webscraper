#include <fstream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

const int MAX_IT = 999999;
vector<bool> digits(10, false);

bool allDigits() {
	for (auto it = digits.begin(); it < digits.end(); it++) {
		if (!*it) {
			return false;
		}
	}
	return true;
}

void logDigits(int num) {
	string str = to_string(num);
	for (auto it = str.begin(); it < str.end(); it++) {
		digits[*it - '0'] = true;
	}
}

int computeCase(istream &is) {
	int n;
	int i;
	is >> n;
	i = 0;
	if (n != 0) {
		while (i < MAX_IT && !allDigits()) {
			i++;
			logDigits(i * n);
		}
		if (i == MAX_IT) {
			i = 0;
		}
	}
	return n * i;
}

int main() {

	ifstream inF("in");
	fstream outF("out", fstream::out);
	int caseCount;
	inF >> caseCount;
	inF.ignore(numeric_limits<streamsize>::max(), '\n');
	for (int caseNum = 1; caseNum <= caseCount; caseNum++) {
		digits = vector<bool>(10, false);
		int caseResult = computeCase(inF);
		outF << "Case #" << caseNum << ": " << (caseResult ? to_string(caseResult) : "INSOMNIA") << endl;
	}
	return 0;

}
