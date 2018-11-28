#include <iostream>

using namespace std;

void tossPancakes();
void reverseStackFrom(int position);

char pancakesStack[100];

void main() {

	int testCases;

	cin >> testCases;

	for (int i = 1; i <= testCases; ++i) {
		cin >> pancakesStack;

		cout << "Case #" << i << ": ";
		tossPancakes();
		cout << endl;
	}
}

void tossPancakes() {
	int tossTimes = 0;

	for (int i = sizeof(pancakesStack) - 1; i >= 0; --i) {
		if (pancakesStack[i] == '-') {
			tossTimes++;
			reverseStackFrom(i);
		}
	}

	cout << tossTimes;
}

void reverseStackFrom(int position) {
	for (int i = position; i >= 0; --i) {
		if (pancakesStack[i] == '-') {
			pancakesStack[i] = '+';
		}
		else {
			pancakesStack[i] = '-';
		}
	}
}
