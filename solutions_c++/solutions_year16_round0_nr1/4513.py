#include <iostream>
#include <ctime>
#define MAX_N 1000000
using namespace std;
bool checkDigits(bool *check, int N) {
	int currentDigit;
	while (N != 0) {
		currentDigit = N % 10;
		check[currentDigit] = true;
		N /= 10;
	}

	for (int i = 0; i < 10; i++) {
		if (check[i] == false)
			return false;
	}
	return true;
}
void calculate(int *finalNumber) {
	for (int i = 0; i <= MAX_N; i++) {
		bool check[10] = { false };
		int currentNumber = i;
		int count = 2;
		while (1) {
			if (i == 0) {
				finalNumber[i] = -1;
				break;
			}
			else if (checkDigits(check, currentNumber)) {
				finalNumber[i] = currentNumber;
				break;
			}
			else {
				currentNumber = i * count;
				count++;
			}
		}
	}
}
int main(void) {
	int *finalNumber = new int[MAX_N + 1];
	calculate(finalNumber);

	int T, N;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N;
		if (finalNumber[N] == -1)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else
			cout << "Case #" << i << ": " << finalNumber[N] << endl;
	}
	return 0;
}