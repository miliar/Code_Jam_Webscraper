// Jai Mata Di
#include <iostream>
using namespace std;
class PancakesStack {
	string sequence;
public:
	void input() {
		cin >> sequence;
	}
	int findSequenceOfConsecutiveSigns() {
		char previousCharacter = sequence[0];
		int numberOfSwitches = 0;
		for (int i = 1; i < sequence.size(); i++) {
			if (sequence[i] != previousCharacter) {
				numberOfSwitches++;
				previousCharacter = sequence[i];
			}
		}
		if (previousCharacter == '-') {
			numberOfSwitches++;
		}
		return numberOfSwitches;
	}
};
int main() {
	int noOfTestCases = 0;
	cin >> noOfTestCases;
	for (int testCaseNo = 1; testCaseNo <= noOfTestCases; testCaseNo++) {
		PancakesStack pancakesStack;
		pancakesStack.input();
		cout << "Case #" << testCaseNo << ": " << pancakesStack.findSequenceOfConsecutiveSigns() << endl;
	}
	return 0;
}
