#include <iostream>
#include <cmath>

using namespace std;


int findLastDigit(unsigned int N) {
	bool digits[10] = {false};
	unsigned char counter = 0;
	unsigned long long tmpRes = N;
	for (unsigned int i = 1; i < 100; i++) {
		tmpRes = N * i;
		for (int j = static_cast<int>(log(tmpRes) / log(10) + 0.0001); j >= 0; j--) {
			if (digits[tmpRes / (int)pow(10, j)] == false) {
				//cerr << tmpRes << ": " << (int)pow(10, j) << ": "<< tmpRes / (int)pow(10, j) << endl;
				counter++;
				if (counter == 10)
					return N * i;
				digits[tmpRes / (int)pow(10, j)] = true;
			}
			tmpRes %= static_cast<int>(pow(10, j));
		}
	}
	return -1;
}

int main () {
	unsigned int T;

	cin >> T;
	unsigned int N[T];
	for (unsigned int i = 0; i < T; i++)
		cin >> N[i];

	int res;
	for (unsigned int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		if ((res = findLastDigit(N[i])) == -1)
			cout << "INSOMNIA";
		else
			cout << res;
		cout << endl;
	}

}