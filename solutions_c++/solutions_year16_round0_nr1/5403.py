#include <iostream>

using namespace std;

int checkCase(int x);
bool checkArray(bool x[10]);

int main() {
	int testCases = 0;
	cin >> testCases;
	int testCasesArr[testCases];
	for(int i = 0; i < testCases; i++) {
		cin >> testCasesArr[i];
	}
	for(int i = 0; i < testCases; i++) {
		int result = checkCase(testCasesArr[i]);
		if(result == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << result << endl;
		}
	}
	
	return 0;
}

int checkCase(int x) {
	bool asdf[10] = {0};
	if(x == 0) {
		return 0;
	} else {
		int curDigit = 0;
		for(int j = 1; j < 1000; j++) {
			for(int curNumber = x * j; curNumber > 0; curNumber /= 10) {
				curDigit = curNumber % 10;
				if(asdf[curDigit] == false) {
					asdf[curDigit] = true;
				}
			}
			if(checkArray(asdf)) {
				return x * j;
			}
		}
		return 0;
	}
}

bool checkArray(bool x[10]) {
	for(int k = 0; k < 10; k++) {
		if(x[k] == false) {
			return false;
		}
	}
	return true;
}
