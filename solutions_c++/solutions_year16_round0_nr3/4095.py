#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;
long long len, J;


bool isPrime(long long n) {
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			return 0;
		}
	}
	return 1;
}

bool check(string s) {
	for (long long i = 2; i <= 10; i++) {
		long long deg = 1;
		long long num = 0;
		for (long long j = 0; j < len; j++) {
			num += deg * (s[j] - '0');
			deg *= i;
		}
		if (isPrime(num)) {
			return 0;
		}
	}
	return 1;
}

void gen(long long left, string s) {
	if (left == 0) {
		if (J > 0 and check(s)) {
			J -= 1;
			reverse(s.begin(), s.end());
			cout << s;
			reverse(s.begin(), s.end());
			for (long long i = 2; i <= 10; i++) {
				long long deg = 1;
				long long num = 0;
				for (long long j = 0; j < len; j++) {
					num += deg * (s[j] - '0');
					deg *= i;
				}
				for (long long j = 2; j < num; j++) {
					if (num % j == 0) {
						cout << " " << j;
						break;
					}
				}
			}
			cout << endl;
		}
		return;
	}
	gen(left-1, s + "1");
	gen(left-1, s + "0");
}

int main() {
	cin >> len;
	cin >> len >> J;
	cout << "Case #1:\n";
	gen(len, "");
	return 0;
}