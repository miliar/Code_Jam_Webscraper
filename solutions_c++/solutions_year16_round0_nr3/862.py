#include <cstdio>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
using namespace std;

long long modpow(long long a, long long r, long long mod) {
	long long ret = 1;
	while (r > 0) {
		if (r % 2 > 0) {
			ret = (ret * a) % mod;
		}
		a = (a * a) % mod;
		r /= 2;
	}
	return ret;
}

bool isPrime(long long n) {
	if (n <= 1 || (n > 2 && n % 2 == 0)) {
		return false;
	}
	if (n == 2 || n == 3) {
		return true;
	}

	mt19937 gen;
	uniform_int_distribution<long long> dis(2, n - 2);
	for (int loop = 0; loop < 20; ++loop) {
		long long pick = dis(gen);
		if (modpow(pick, n - 1, n) != 1) {
			return false;
		}
	}
	return true;
}

int n = 16;
int state[100];
vector<string> anslist;

void rec(int step) {
	if (step >= n - 1) {
		bool ok = true;
		for (int base = 2; base <= 10; ++base) {
			long long ret = 0, coff = 1;
			for (int i = n - 1; i >= 0; --i) {
				ret += state[i] * coff;
				coff *= base;
			}

			if (isPrime(ret)) {
				ok = false;
				break;
			}
		}
		if (ok) {
			string res = "";
			for (int i = 0; i < n; ++i) {
				res += to_string(state[i]);
			}
			anslist.push_back(res);
		}
		return;
	}

	state[step] = 0;
	rec(step + 1);
	if (anslist.size() >= 200) {
		return;
	}
	state[step] = 1;
	rec(step + 1);
}

const int PMAX = 10000000;
bool notPrime[PMAX + 1];
vector<int> primes;

int main() {
	freopen("output.txt", "w", stdout);

	for (int i = 2; i <= PMAX; ++i) {
		if (notPrime[i]) {
			continue;
		}
		primes.push_back(i);
		for (int j = i + i; j <= PMAX; j += i) {
			notPrime[j] = true;
		}
	}

	state[0] = state[n - 1] = 1;
	rec(1);

	printf("Case #1:\n");
	int printCnt = 0;
	for (const auto& s : anslist) {
		bool ok = true;
		vector<int> divlist;
		for (int base = 2; base <= 10; ++base) {
			long long num = 0, coff = 1;
			for (int j = s.length() - 1; j >= 0; --j) {
				num += coff * (s[j] - '0');
				coff *= base;
			}

			int q = -1;
			for (int p : primes) {
				if (num % p == 0) {
					q = p;
					break;
				}
			}
			if (q == -1) {
				ok = false;
				break;
			}
			divlist.push_back(q);
		}
		if (!ok) {
			continue;
		}

		printf("%s", s.c_str());
		for (int div : divlist) {
			printf(" %d", div);
		}
		printf("\n");
		++printCnt;
		if (printCnt >= 50) {
			break;
		}
	}

	return 0;
}