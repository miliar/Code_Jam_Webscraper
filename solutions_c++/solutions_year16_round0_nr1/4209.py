#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	long long N;
	long long currentResult;
	int digitsFound[10];
	int numDigitsFound;
	for(int count = 1; count <= T; ++count) {
		cin >> N;
		if(N == 0) {
			cout << "Case #" << count << ": " << "INSOMNIA" << endl;
			continue;
		}

		numDigitsFound = 0;
		for(int i = 0; i < 10; ++i) {
			digitsFound[i] = 0;
		}

		currentResult = 0;
		while (numDigitsFound < 10) {
			currentResult = currentResult + N;
			long long temp = currentResult;
			int digit;
			while(temp > 0) {
				digit = temp % 10;
				if(digitsFound[digit] == 0) {
					digitsFound[digit] = 1;
					numDigitsFound = numDigitsFound + 1;
				}

				temp = temp / 10;
			}

		}

		cout << "Case #" << count << ": " << currentResult << endl;

	}

	return 0;
}