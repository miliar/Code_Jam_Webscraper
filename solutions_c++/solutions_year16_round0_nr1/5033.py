#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

int main() {
	int T, N;
	bool digits[10];
	long long multiplier, count, value, work, digit;

	cin >> T;
	for(int t=0; t<T; t++) {
		memset(digits, 0, sizeof(digits));
		cin >> N;

		if(N==0) {
			cout << "Case #" << (t+1) << ": INSOMNIA" << endl;
		} else {
			for(multiplier = 1, count = 0; count < 10; multiplier++) {
				value = work = multiplier * N;
				while(work > 0) {
					digit = work % 10;
					if(!digits[digit]) {
						digits[digit] = 1;
						count++;
					}

					work /= 10;
				}
			}

			cout << "Case #" << (t+1) << ": " << value << endl;
		}
	}

	return 0;
}
