#include <iostream>

using namespace std;

//long long ipow(long long base, long long exp) {
//	while (exp) {
//
//	}
//}

long long ipow(long long base, long long exp)
{
	long long result = 1;
	while (exp)
	{
		if (exp & 1)
			result *= base;
		exp >>= 1;
		base *= base;
	}

	return result;
}

int main() {
	int cases;

	cin >> cases;

	for (int i = 1; i <= cases; i++) {
		int k, c, s;
		cin >> k >> c >> s;

		if (k != s) {
			cout << "Lies!" << endl;
			exit(1);
		}

		//long long incr = ipow(k, c - 1);
		cout << "Case #" << i << ":";
		for (int j = 0; j < s; j++) {
			long long ans = 0;
			for (int jj = 0; jj < c; jj++) {
				ans *= k;
				ans += j;
			}
			cout << " " << ans + 1;
		}
		cout << endl;
	}

	return 0;
}