#include <bits/stdc++.h>

using namespace std;

long long divisor(long long n) {
	for(long long i = 2; i*i <= n; i ++) {
		if(n % i == 0) {
			return i;
		}
	}

	return 0;
} 

long long baseconv(long long n, long long b) {
	long long res = 0;
	long long mult = 1;

	while(n != 0) {
		if(n & 1) {
			res += mult;
		}

		n >>= 1;
		mult *= b;
	}

	return res;
}

void printbin(long long n) {
	stringstream s;
	while(n != 0) {
		s << (n & 1);
		n >>= 1;
	}

	string a = s.str();
	reverse(a.begin(), a.end());

	cout << a;
}

void solve(int nn, int j) {
	cout << endl;

	long long divisors[9];

	long long n = (1ll << (nn - 1)) + 1;
	while(j > 0) {
		//cout << "n" << n << endl;
		bool valid = true;
		for(int i = 2; i <= 10; i++) {
			long long m = divisor(baseconv(n, i));
			if(m) {
				divisors[i-2] = m;
			}
			else {
				valid = false;
				break;
			}
		}
		if(valid) {
			printbin(n);
			for(int i = 0; i < 9; i++) {
				cout << " " << divisors[i];
			}
			cout << endl;

			j--;
		}

		n += 2;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		int n, j;
		cin >> n >> j;

		solve(n, j);
	}

	return 0;
}
