#include <iostream>
using namespace std;

int main() {

	int numberOfInputs, N, result = 0;
	cin >> numberOfInputs;

	bool digits[10];
	bool ones[10];
	memset(ones, true, 10);

	for (int input = 1; input <= numberOfInputs; input++) {
		cin >> N;
		memset(digits, false, 10);

		if (N == 0) {
			cout << "Case #" << input << ": INSOMNIA" << endl;
		}
		else {
			
			int i = 1;
			for (i = 1; memcmp(digits, ones, 10 * sizeof(bool)); i++) {
				int NN = i * N;
				while (NN > 0) {
					digits[NN % 10] = true;
					NN /= 10;
				}
			}

			result = N * (i-1);

			cout << "Case #" << input << ": " << result << endl;
		}
	}

	return 0;
}