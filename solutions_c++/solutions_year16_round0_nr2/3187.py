#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
	int nTestCases;
	cin >> nTestCases;

	for (int i = 0; i < nTestCases; ++i) {
		string states;
		cin >> states;

		int flipTimes = 0;
		for (int s = states.length() - 1; s >= 0; s--) {
			if (flipTimes % 2 != 0 && states.at(s) == '+') {
				flipTimes++;
			} else if (flipTimes %2 == 0 && states.at(s) == '-') {
				flipTimes++;
			}
		}
		cout << "Case #" << i+1 << ": " << flipTimes << endl;	
	}

	return 0;
}