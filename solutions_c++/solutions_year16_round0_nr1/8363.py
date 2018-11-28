#include <iostream>
#include <vector>

using namespace std;

bool isInVector(unsigned __int64 number, vector<unsigned __int64> v) {
	if (v.size() != 0) {
		for (unsigned int i = 0; i < v.size(); i++) {
			if (v.at(i) == number) {
				return true;
			}
		}
	}
	return false;
}

int sumOfArray(int numbers[10]) {
	int sum = 0;
	for (int i = 0; i < 10; i++) {
		sum += numbers[i];
	}
	return sum;
}

int main() {
	int testCases;
	cin >> testCases;
	vector<unsigned __int64> v;
	int numbers[10];
	bool insomnia;

	for (int testCase = 1; testCase <= testCases; testCase++) {
		unsigned __int64 initNumber;
		unsigned __int64 number;
		insomnia = false;
		v.clear();
		for (int i = 0; i < 10; i++) {
			numbers[i] = 0;
		}

		cin >> initNumber;
		number = initNumber;

		while (true) {
			if (isInVector(number, v)) {
				insomnia = true;
				break;
			}
			
			v.push_back(number);
			unsigned __int64 n = number;

			while (n > 9) {
				numbers[n % 10] = 1;
				n = n / 10;
			}
			numbers[n] = 1;
			if (sumOfArray(numbers) == 10) {
				break;
			}
			number += initNumber;
		}

		if (insomnia) {
			printf("Case #%d: INSOMNIA\n", testCase);
		}
		else {
			printf("Case #%d: %llu\n", testCase, number);
		}

	}
}