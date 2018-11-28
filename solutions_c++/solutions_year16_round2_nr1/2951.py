#include <iostream>
#include <map>

using namespace std;

int main(int argc, char const *argv[]) {
	int nTestCases;
	cin >> nTestCases;

	for (int i = 0; i < nTestCases; ++i) {
		string S;
		cin >> S;

		map<char, int> charCount;
		std::map<char,int>::iterator it;

		for (int cid = 0; cid < S.length(); ++cid) {
			char c = S.at(cid);
			it = charCount.find(c); 
			if (it == charCount.end()) {
				charCount[c] = 1;
			} else {
				charCount[c] += 1;
			}
		}

		int numCount[10];
		numCount[0] = charCount['Z'];
		numCount[1] = charCount['O'] - charCount['Z'] - charCount['W'] - charCount['U'];
		numCount[2] = charCount['W'];
		numCount[3] = charCount['R'] - charCount['Z'] - charCount['U'];
		numCount[4] = charCount['U'];
		numCount[5] = charCount['F'] - charCount['U'];
		numCount[6] = charCount['X'];
		numCount[7] = charCount['V'] - numCount[5];
		numCount[8] = charCount['G'];
		numCount[9] = charCount['I'] - charCount['G'] - numCount[5] - numCount[6];

		cout << "Case #" << i+1 << ": ";
		for (int num = 0; num < 10; ++num) {
			for (int count = 0; count < numCount[num]; ++count) {
				cout << num;
			}
		}
		cout << endl;	
	}

	return 0;
}