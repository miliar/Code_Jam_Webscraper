#include <iostream>

using namespace std;

void printLastSawNumber();
bool checkIfStillCounting(bool* sawNumbers);

int baseNumber;

void main() {

	int testCases;

	cin >> testCases;

	for (int i = 1; i <= testCases; ++i) {
		cin >> baseNumber;

		cout << "Case #" << i << ": ";
		printLastSawNumber();
		cout << endl;
	}
}

void printLastSawNumber() {
	bool sawNumbers[10] = { 
		false, 
		false, 
		false, 
		false, 
		false,
		false,
		false,
		false,
		false,
		false
	};
	int lastSawNumber;

	if (baseNumber * 2 == baseNumber) {
		cout << "INSOMNIA";
		return;
	}

	bool isStillCounting = true;

	for (int i = 1; isStillCounting; ++i) {
		int numberToCompute = baseNumber * i;
		lastSawNumber = numberToCompute;

		while (numberToCompute > 0) {
			int sawNumber = numberToCompute % 10;
			sawNumbers[sawNumber] = true;
			numberToCompute /= 10;
		}
		isStillCounting = checkIfStillCounting(sawNumbers);
	}

	cout << lastSawNumber;
}

bool checkIfStillCounting(bool* sawNumbers) {
	for (int i = 0; i < 10; ++i) {
		if (sawNumbers[i] == false) {
			return true;
		}
	}
	return false;
}