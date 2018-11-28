#include <iostream>
#include <string>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	for (int caseNum = 1; caseNum <= numCases; ++caseNum) {
		string stack;
		cin >> stack;
		int numFlips = 0;
		for (int i = 1; i < stack.size(); ++i) {
			if (stack[i] != stack[i-1]) numFlips++;
		}
		if (stack[stack.size()-1] == '-') numFlips++;
		cout << "Case #" << caseNum << ": " << numFlips << endl;
	}
	
	return 0;
}
