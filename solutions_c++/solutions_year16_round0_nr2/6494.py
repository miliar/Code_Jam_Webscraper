#include <iostream>
#include <vector>
#include <cstring>
#include <sstream>

using namespace std;

int main() {
	int numTestCases = 0;
	cin >> numTestCases;
	string sentence;
	getline(cin,sentence);
	for (int i = 0; i < numTestCases; i++) {
		string sentence;
		getline(cin,sentence);
		int numberOfFlips = 0;
		bool lookForPlus = false;
		for (int i = sentence.length()-1; i>=0; i--) {
			if (lookForPlus) {
				if (sentence[i] == '+') {
					numberOfFlips++;
					lookForPlus = !lookForPlus;
				}
			} else {
				if (sentence[i] == '-') {
					numberOfFlips++;
					lookForPlus = !lookForPlus;
				}
			}
        }
		cout << "Case #" << i+1 << ": " << numberOfFlips << endl;
	}
	return 0;
}