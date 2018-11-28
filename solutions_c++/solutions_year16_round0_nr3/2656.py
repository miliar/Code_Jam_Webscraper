// Problem C. Coin Jam
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

vector<long long> primes;

void sieve_primes(char p[], int n)
{
	long long i, j;
	memset(p, 1, n * sizeof(p[0]));
	for (p[0] = p[1] = 0, i = 2; i * i < n; i++)
		if (p[i]) for (j = i * i; j < n; j += i) p[j] = 0;
}

long long test_prime(long long x)
{
	for (int i = 0; i < primes.size(); i++) {
		long long p = primes[i];
		if (p * p > x) break;
		if (x % p == 0) return p;
	}
	return 0;
}

int main(int argc, char *argv[])
{
	static char p[32000000];
	sieve_primes(p, sizeof(p));
	for (int i = 2; i < sizeof(p); i++)
		if (p[i]) primes.push_back(i);

	int T;
	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N, J;
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", ti);
		long long y = 1 + (1 << (N - 1)), z = (1 << N);
		int count = 0;
		for ( ; y < z && count < J; y += 2) {
			bool ok = true;
			vector<long long> a;
			for (long long b = 2; b <= 10; b++) {
				long long x = 0, t = 1;
				for (int i = 0; i < N; i++, t *= b)
					if (y & (1 << i)) x += t;
				t = test_prime(x);
				if (t == 0) {
					ok = false;
					break;
				}
				a.push_back(t);
			}
			if (!ok) continue;
			count++;

			for (int i = N - 1; i >= 0; i--) printf("%d", (y & (1 << i)) ? 1 : 0);
			for (int i = 0; i < a.size(); i++) printf(" %lld", a[i]);
			printf("\n");
		}
	}

	return 0;
}
