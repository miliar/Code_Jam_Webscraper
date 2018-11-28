#include <bits/stdc++.h>
#include <stdlib.h>

using namespace std;

long long finddiv(long long x) {
	if (x % 2 == 0) return 2;

	for (int i = 3; i <= sqrt(x); i += 2) {
		if (x % i == 0) return i;
	}

	return -1;
}

long long fpow(long long b, int e) {
	long long value = 1;
	while (e) {
		if (e & 1) value *= b;
		b *= b;
		e >>= 1;
	}
	return value;
}

string tobin(long long val) {
	string ret;
	while (val) {
		ret += '0' + (val & 1);
		val >>= 1;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);

	printf("Case #1:\n");

	int N, J;
	scanf("%d%d", &N, &J);

	long long top = fpow(2, N) - 1;

	string jamcoin;
	int divs[10];
	int found = 0;

	for (long long i = 1 + fpow(2, N-1); i <= top; i+=2) {
		jamcoin = tobin(i);
		int m = 0;

		for (int b = 2; b < 11; b++) {
			long long n = 0;
			if (b > 2) {
				for (int j = 0; j < jamcoin.size(); j++) {
					if (jamcoin[jamcoin.size() - j - 1] == '1') {
						n += fpow(b, j);
					}
				}
			} else n = i;

			divs[m++] = finddiv(n);
			if (divs[m-1] == -1) {				
				m = 0;
				break;
			}
		}

		if (m) {
			found++;
			printf("%s ", jamcoin.c_str());
			for (int j = 0; j < m; j++) {
				printf("%d ", divs[j]);
			}
			printf("\n");

			if (found == J) {
				break;
			}
		}
	}

	return 0;
}