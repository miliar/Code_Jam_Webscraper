#include <iostream>
using namespace std;

bool *digits;

bool allDigitsUsed () {
	for (int i = 0; i < 10; i++) {
		if (!digits[i]) {
			return false;
		}
	}
	
	return true;
}

int myFunc (int pick) {
	if (pick == 0) { // base case
		return -1;
	} 
	
	for (int i = 0; i < 10; i++) {
		digits[i] = false;
	}
	
	int currentVal = pick;
	
	int counter = 0;
	while (true) {
		
		int testVal = currentVal;
		int divisor = 10;
		while (testVal > 0) {
			int remainder = testVal % divisor;
			if (!digits[remainder]) {
				digits[remainder] = true;
				// cout << "got " << remainder << cout;
				if (allDigitsUsed()) {
					return currentVal;
				}
			}
			testVal /= divisor;
		}
		
		// cout << "counter: " << counter << ", tried" << currentVal << endl;
		currentVal += pick;
		counter ++;
	}
	
}

int main (int argc, char *argv[]) {
	
	digits = new bool [10];
	int numTestCases;
	cin >> numTestCases;
	
	for (int i = 0; i < numTestCases; i++) {
		int targetNum;
		cin >> targetNum;
		int result = myFunc(targetNum);
		
		if (result == -1) {
			cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
		} else {
			cout << "Case #" << (i + 1) << ": " << result << endl;
		}
	}
	
	delete[] digits;
	
	return 0;
}
