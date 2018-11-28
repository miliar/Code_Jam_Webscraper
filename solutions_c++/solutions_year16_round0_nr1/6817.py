#include <iostream>

using namespace std;

void runTestCase(long long i);
bool checkDigits(bool digits[]);

int main() {

	long long t = 0;

	cin >> t;

	for (long long i = 0; i < t; i++) {
		runTestCase(i);
	}

	return 0;
}

void runTestCase(long long i) {
	
	cout << "Case #" << i + 1 << ": ";
	
	long long x = 0;
	cin >> x;
	
	if (x == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}

	long long last = x;
	bool digits[10];

	for (long long j = 0; j < 10; j++)
		digits[j] = false;

	for (long long j = 1; j < 100; j++) {
		long long tmp = last;

		do {
			digits[tmp % 10] = true;
			tmp /= 10;
		} while (tmp > 0);

		if (checkDigits(digits))
			break;

		last = x * j;
	}

	cout << last << endl;
}

bool checkDigits(bool digits[]) {

	bool isComplete = true;

	for (long long i = 0; i < 10; i++) {
		if (!digits[i]) {
			isComplete = false;
			break;
		}
	}

	return isComplete;
}


