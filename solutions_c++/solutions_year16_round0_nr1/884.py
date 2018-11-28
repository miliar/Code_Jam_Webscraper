#include <iostream>
using namespace std;

int pow10[8] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };

int digitCountIn(int n) {
	for (int d = 1; d <= 6; d++)
		if (pow10[d] > n)
			return d;
	return 6;
}

int lastNumberNamed(int n) {
	if (n == 0)
		return -1;
	int d = digitCountIn(n);
	int m = 0;
	int seenCount = 0;
	bool seen[10] = { false, false, false, false, false, false, false, false, false, false };
	for (int i = 1; i <= pow10[d + 1]; i++) {
		m += n;
		for (int digits = m; digits; digits /= 10) {
			int dig = digits % 10;
			if (!seen[dig]) {
				seenCount++;
				if (seenCount == 10)
					return m;
				seen[dig] = true;
			}
		}
	}
	return -1;
}

int main() {
	int cases;
	cin >> cases;
	for (int caseCounter = 1; caseCounter <= cases; caseCounter++) {
		int n;
		cin >> n;
		int lastNumber = lastNumberNamed(n);
		if (lastNumber == -1)
			cout << "Case #" << caseCounter << ": INSOMNIA" << endl;
		else
			cout << "Case #" << caseCounter << ": " << lastNumber << endl;
	}
	return 0;
}
