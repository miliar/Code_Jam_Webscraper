#include <iostream>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

bool isPali(int n) {
	int digits[20];
	int q = n;
	int len = 0;
	while (q > 0) {
		digits[len++] = q%10;
		q/= 10;
	}
	for (int j = 0; j < len; j++) {
		if (digits[j] != digits[len-j-1])
			return false;
	}
	return true;
}
int main() {
	int t;
	ull a, b;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> a >> b;
		ull counter = 0;
		ull sqa = ceil(sqrt(a)), sqb = sqrt(b);
		for (ull i = sqa; i <= sqb; i++) {
			if (isPali(i) && isPali(i*i))
				counter++;
		}
		cout << "Case #" << test << ": " << counter << endl;
	}

	return 0;
}
