// Compiler verion : GCC 5.2.1
// Language: C++ 14

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

const int DIGIT = 10;
const int MAXCASE = 100;

int mCheck[DIGIT];
int countDigit(int number) {
	int count = 1;
	for (;pow(10, count) - 1 < number; count++);
//	cout << "countDigit: " << count << endl;
	return count;
}

bool fallingAsleep() {
	for(int i = 0; i < DIGIT; i++) {
		if (mCheck[i] < 0)
			return false;
	}
	return true;
}

int countingSheep(int number) {
	if (number == 0) {
		return -1; // INSOMNIA
	}

	int resultNumber = number;

	for (int i = 1; i < MAXCASE; i++) {

		int count = countDigit(resultNumber);
		for (int j = count, tempNumber = resultNumber; j > 0; j--) {
			int expDecimal = pow(10, j - 1);
//			cout << "tempNumber: " << tempNumber << " expDecimal: " << expDecimal << endl;
			int digit = tempNumber / expDecimal;
			mCheck[digit] = 1;
			tempNumber = tempNumber - (digit * expDecimal);
//			cout << "digit: " << digit << " tempNumber: " << tempNumber << endl;
		}

		if(fallingAsleep())
			return resultNumber;

		resultNumber = number * i;
	}

	return -1;
}

void initDigit() {
	for (int i = 0; i < DIGIT; i++) {
		mCheck[i] = -1;
	}
}

int main()
{
	fstream fInput("A-small-attempt0.in");
	string line = "";

	while (getline(fInput, line)) {
		// the number of cases
		int cases = stoi(line);
//		cout << cases << endl;

		for (int i = 0; i < cases; i++) {
			getline(fInput, line); //get a credit
			int number = stoi(line);
//			cout << number << endl;
			initDigit();
			int result = countingSheep(number);
			cout << "Case #" << i+1 << ": ";
			if (result < 0)
				cout << "INSOMNIA" << endl;
			else
				cout << result << endl;
		}
	}
	return 0;
}
