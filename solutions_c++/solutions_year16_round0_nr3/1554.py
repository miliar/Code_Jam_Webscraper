#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <assert.h>

using namespace std;

typedef vector<int> lnum;
const int lbase = 1000 * 1000 * 1000;

void add(lnum& a, const lnum& b)
{
	int carry = 0;
	for (size_t i = 0; i<max(a.size(), b.size()) || carry; ++i) {
		if (i == a.size())
			a.push_back(0);
		a[i] += carry + (i < b.size() ? b[i] : 0);
		carry = a[i] >= lbase;
		if (carry)  a[i] -= lbase;
	}
}

void mul(lnum& a, int b)
{
	int carry = 0;
	for (size_t i = 0; i<a.size() || carry; ++i) {
		if (i == a.size())
			a.push_back(0);
		long long cur = carry + a[i] * 1ll * b;
		a[i] = int(cur % lbase);
		carry = int(cur / lbase);
	}
	while (a.size() > 1 && a.back() == 0)
		a.pop_back();
}

void strtolnum(const string& s, lnum& a, int base)
{
	a.clear();
	lnum pow = { 1 };
	for (int i = s.length() - 1; i >= 0; i--) {
		if (s[i] == '1') {
			add(a, pow);
		}
		mul(pow, base);
	}
}

int div(lnum& a, int b)
{
	int carry = 0;
	for (int i = (int)a.size() - 1; i >= 0; --i) {
		long long cur = a[i] + carry * 1ll * lbase;
		a[i] = int(cur / b);
		carry = int(cur % b);
	}
	while (a.size() > 1 && a.back() == 0)
		a.pop_back();
	return carry;
}

void test()
{
	int N, J;
	cin >> N >> J;

	int n_prime = 2000;
	vector<bool> prime(n_prime + 1, true);
	prime[0] = prime[1] = false;
	for (int i = 2; i <= n_prime; ++i)
		if (prime[i])
			if (i * 1ll * i <= n_prime)
				for (int j = i*i; j <= n_prime; j += i)
					prime[j] = false;
	vector<int> primes;
	for (int i = 2; i <= n_prime; ++i) {
		if (prime[i]) primes.push_back(i);
	}

	string s(N, '0');
	s[0] = '1';
	int k = 0;
	while (true) {
		if (s[s.length() - 1] == '1') {
			bool isJamcoin = true;
			vector<int> divisors(11, 0);
			for (int base = 2; base <= 10; base++) {
				lnum x;
				strtolnum(s, x, base);
				bool isPrime = true;
				for (int p : primes) {
					lnum xcopy = x;
					int carry = div(xcopy, p);
					if (carry == 0) {
						divisors[base] = p;
						isPrime = false;
						break;
					}
				}
				if (isPrime) {
					isJamcoin = false;
					break;
				}
			}
			if (isJamcoin) {
				cout << endl << s;
				for (int base = 2; base <= 10; base++) {
					cout << " " << divisors[base];
				}
				k++;
				if (k >= J) break;
			}
		}

		int carry = 1;
		for (int i = s.length() - 1; i >= 0; i--) {
			int sum = (s[i] - '0') + carry;
			s[i] = sum % 2 + '0';
			carry = sum / 2;
			if (carry == 0) break;
		}
	}
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		//cout << endl;
	}
	return 0;
}
