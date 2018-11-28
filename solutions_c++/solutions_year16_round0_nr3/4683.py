#include <sstream>
#include <iostream>
#include <stdio.h>

using namespace std;

long long validCoins[52][11];

string binaryToString(int number) {
	string s = "";
	while (number) {
		s = (char) ((number % 2) + '0') + s;
		number /= 2;
	}
	return s;
}

long long getDivisor(int number, int base) {
	long long numberInBase = 0;
	if (base == 2) {
		numberInBase = number;
	} else {
		long long power = 1ll;
		while (number) {
			numberInBase += (number % 2) * power;
			power *= base;
			number /= 2;
		}
	}
	for (long long i = 3; i * i <= numberInBase; i++) {
		if (!(numberInBase % i))
			return i;
	}
	return -1;
}

void generateJamCoin(int n, int j) {
	int curValid = 0;
	for (int i = ((1 << (n - 1)) + 1); i < 1 << n; i += 2) {
		if (curValid > j)
			return;
		int base = 2;
		while (base < 11) {
			long long divisor = getDivisor(i, base);
			if (divisor == -1) {
				break;
			}
			validCoins[curValid][base++] = divisor;
		}
		if (base == 11) {
			validCoins[curValid][0] = i;
			curValid++;
		}
	}
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int N, J, T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		scanf("%d %d", &N, &J);
		generateJamCoin(N, J);
		printf("Case #%d:\n", t + 1);
		for (int i = 0; i < J; ++i) {
			cout << binaryToString(validCoins[i][0]);
			for (int j = 2; j <= 10; ++j) {
				cout << " " << validCoins[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
