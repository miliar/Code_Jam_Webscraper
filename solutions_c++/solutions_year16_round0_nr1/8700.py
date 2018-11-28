#include <bits/stdc++.h>

using namespace std;

int main() {
	int nCase;
	cin >> nCase;

	for (int i = 1; i <= nCase; ++i) {
		cout << "Case #" << i << ": ";
		int number;
		cin >> number;

		int filled = 0;
		for (int j = 1; j < 200000; ++j) {
			int tempC = number * j;
			while (tempC > 0) {
				filled |= 1 << (tempC % 10);
				tempC /= 10;
			}
			if (filled == ((1 << 10) - 1)) {
				cout << number * j << endl;
				break;
			}
		}
		if (filled != ((1 << 10) - 1)) {
			cout << "INSOMNIA" << endl;
		}
	}

	return 0;
}
