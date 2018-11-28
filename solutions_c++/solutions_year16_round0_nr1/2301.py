#include <iostream>

using namespace std;


int getResult(int n) {
	if(n == 0) return -1;

	int remainingDigits = 10;
	bool digitSeen[10] = {0};

	int currentNumber = n;

	while(remainingDigits > 0) {
		int aux = currentNumber;
		while(aux) {
			int curDigit = aux%10;
			if(!digitSeen[curDigit]) {
				remainingDigits --;
				digitSeen[curDigit] = true;
			}
			aux /= 10;
		}
		currentNumber += n;
	}

	return currentNumber - n;

}

int main() {
	int noTests;
	cin >> noTests;

	for(int i = 0; i < noTests; ++i) {
		int N;
		cin >> N;

		int result = getResult(N);
		if(result < 0) {
			cout << "Case #" << i+1 << ": " << "INSOMNIA\n";
		}
		else {
			cout <<"Case #" << i+1 << ": " << result << "\n";
		}
	}
}