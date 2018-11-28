#include <iostream>
#include <cmath>
#include <string>

using namespace std;

#define N 16
#define J 50

bool isPrime(long long x, long long &div) {
	long long sr = (long long) sqrt(x) + 1;
	for (long long i = 2; i <= sr; i++) {
		if (x % i == 0) {
			div = i;
			return false;
		}
	}
	return true;
}

long long convertToBase10(long long x, int base) {
	long long result = 0;
	long long mult = 1;
	while (x) {
		result += (x % 10) * mult;
		x /= 10;
		mult *= base;
	}
	return result;
}

bool isJamcoin(string x) {
	if (x[0] == '0') return false;
	if (*(x.rbegin()) == '0') return false;

	long long n = 0;
	string::iterator it = x.begin();
	while (it != x.end()) {
		n = n * 10 + (*it - '0');
		it++;
	}

	for (int i = 2; i <= 10; i++) {
		long long div, r = convertToBase10(n, i);
		if (isPrime(r, div)) return false;
	}

	return true;
}

bool allOnes(string x) {
	for (int i = 0; i < N; i++) {
		if (x[i] == '0') return false;
	}
	return true;
}

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	cout << "Case #1:" << endl;

	string x(N, '0');
	int j = 0;

	while (!allOnes(x)) {
		int i = N - 1;
		x[i] = x[i] + 1;
		while (x[i] == '2') {
			x[i] = '0';
			i--;
			x[i] = x[i] + 1;
		}
	
		if (isJamcoin(x)) {
			cout << x;

			long long n = 0;
			string::iterator it = x.begin();
			while (it != x.end()) {
				n = n * 10 + (*it - '0');
				it++;
			}

			for (int i = 2; i <= 10; i++) {
				long long div, r = convertToBase10(n, i);
				isPrime(r, div);
				cout << " " << div;
			}	

			cout << endl;

			j++;
			if (j == J) break;
		}
	}
	
	return 0;
}