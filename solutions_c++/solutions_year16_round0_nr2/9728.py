#include <iostream>
#include <stack>
#include <string>
using namespace std;

char getFlip(char pck) {
	char flip = pck == '-' ? '+' : '-';
	return flip;
}

int countFlips(string pancakeStk) {
	int flipN = 0;
	while (pancakeStk.length() > 1 || pancakeStk[0] == '-') {
		char first = pancakeStk[0], firstFlip = getFlip(first);
		size_t pos = pancakeStk.find_first_of(firstFlip);
		if (pos == string::npos) {
			if (first == '-')
				flipN++;
			break;
		}
		string replaceStr = "";
		replaceStr.push_back(firstFlip);
		pancakeStk.replace(0, pos, replaceStr);
		flipN++;
	}
	return flipN;
}

int main() {
	int caseN;
	string pancakeStack;
	cin >> caseN;
	for (int i = 1; i <= caseN; i++) {
		cin >> pancakeStack;
		cout << "Case #" << i << ": ";
		cout << countFlips(pancakeStack) << endl;
	}
	return 0;
}