#include "bits/stdc++.h"

using namespace std;

vector<int> primes;
vector<unsigned int> rem[11];
int N;
unsigned long long convert(unsigned int n, int base) {
	unsigned long long res = 0;
	unsigned long long s = 1;
	for (int i = 0; i < N; i++) {
		if (n & (1<<i)) {
			res += s;
		}
		s *= base;
	}
	return res;
}

bool test(unsigned int n) {
	unsigned long long a[11];
	unsigned int nold = n;
	for (int k = 2; k <= 10; k++) {
		unsigned long long conv = convert(n, k);
		bool isP = true;
		for (int i = 0; i <  primes.size() /*&& (unsigned long long) primes[i] * primes[i] <= conv*/; i++) {
			//if (conv + rem[k][i] != convert(n + (1<<(N-1)), k))  {
				//cerr << conv + rem[k][i] << " != " << convert(n + (1<<(N-1)), k) << std::endl;
			//}
			if ((conv + rem[k][i]) % (unsigned long long)primes[i] == 0) {
				a[k] = (unsigned long long)primes[i];
				isP = false;
				break;
			}
		}

		if (isP) {
			//cout << "Seems " << n << " is a prime" << std::endl;
			return false;
		}
	}
	char buffer[100];
	for (int x = 0; x < 100; x++) buffer[x] = '0';
	buffer[99] = 0;
	buffer[99-N] = '1';
	int l = 98;
	while (n > 0) {
		if (n % 2 == 1) {
			buffer[l--] = '1';
		} else {
			buffer[l--] = '0';
		}
		n /= 2;
	}
	cout << &buffer[99-N];
	for (int k = 2; k <= 10; k++) {
		cout << " " << a[k];
	}
	cout << endl;
	return true;
}

int main() {
	int c = 3;
	int t, n, j;
	cin >> t >> n >> j;
	N = n;
	while(c < 100000000) {
		bool a = true;
		for (int i = 0; i <  primes.size() && primes[i] * primes[i] <= c; i++) {
			if (c % primes[i] == 0) {
				a = false;
				break;
			}
		}
		if (a) {
			primes.push_back(c);
			for (unsigned int y = 2; y <= 10; y++) {
				unsigned long long remain = 1;
				for(int x = 0; x < N-1; x++) {
					remain = (remain * y) % c;
				}
				rem[y].push_back((unsigned int) remain);
			}
		}
		c+=2;
	}
	unsigned int cur = /*(1<<(n-1)) +*/ 1;
	printf("Case #1:\n");
	while(j > 0) {
		if (test(cur)) j--;
		cur += 2;
	}
}
