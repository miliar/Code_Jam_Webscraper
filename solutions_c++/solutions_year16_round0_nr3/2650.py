#include <iostream>
#include <math.h>

using namespace std;

long long dectobin(int decimal) {
	int binary = 0, times = 0;
	while(decimal > 0) {
		int cur = decimal % 2;
		if (cur == 1)
		{
			binary += pow(10, times);
		}
		times++;
		decimal /= 2;
	}
	return binary;
}

long long digittoresult(long long digit) {
	long long result = 0, times = 0;
	while(digit > 0) {
		int cur = digit % 10;
		if (cur == 1)
		{
			result += 11 * pow(100, times);
		}
		times++;
		digit /= 10;
	}

	return result;
}

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
			int N, J, curdigit = 1;
			cin >> N >> J;

			cout << "Case #" << i + 1 << ":" << endl;

			while(curdigit <= J) {
				long long binary = dectobin(curdigit);
				long long result = digittoresult(binary);
				result += 11 * pow(10, (N - 4));
				result *= 100;
				result += 11;

				cout << result << " 3 4 5 6 7 8 9 10 11" << endl;

				curdigit++;
			}

	}

	return 0;
}