#include <bits/stdc++.h>

using namespace std;

void noteDigits(bitset<10>& seenDigits, long M) {
	while (M>0) {
		int digit = M%10;
		seenDigits[digit] = 1;
		M = (M-digit)/10;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		int N;
		cin >> N;
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else {
			bitset<10> seenDigits;
			long M = N;
			noteDigits(seenDigits, M);
			while (!seenDigits.all()) {
				M += N;
				noteDigits(seenDigits, M);
			}
			cout << M << endl;
		}
	}
	return 0;
}