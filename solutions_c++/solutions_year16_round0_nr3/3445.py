#include <cstdio>
#include <iostream>
#include <cassert>
#include <vector>
using namespace std;

long long isPrime(long long n) {
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0)
			return i;
	}
	return 0;
}

int main(void) {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N = 16;
	int J = 50;

	int endsMask = (1 << (N - 1)) + 1;
	int numJamCoins = 0;
	cout << "Case #1:\n";
	for (int mask = 0; mask < (1 << N) && numJamCoins < J; mask++) {
		if ((mask & endsMask) != endsMask)
			continue;

		vector<int> v;
		bool nonePrime = true;
		for (int b = 2; b <= 10 && nonePrime; b++) {
			long long val = 0;
			for (int i = 0; i < N; i++) {
				val = val * b + ((mask & (1 << (N - i - 1))) > 0);
			}

			int p = isPrime(val);
			if (p == 0)
				nonePrime = false;
			else
				v.push_back(p);
		}
		
		if (nonePrime) {
			for (int i = 0; i < N; i++) {
				cout << ((mask & (1 << (N - 1 - i))) > 0);
			}

			for (int i = 0; i < v.size(); i++) {
				cout << ' ' << v[i];
			}
			cout << '\n';
			numJamCoins++;
		}
	}

	assert(numJamCoins == J);

	return 0;
}
