#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>

using namespace std;

const long long sz = 16;
const long long mx = (1LL << sz) - 1LL;

const long long trivial_limit = 50;
long long p[1000];

long long gcd(long long a, long long b) {
	return a ? gcd(b%a, a) : b;
}

long long powmod(long long a, long long b, long long m) {
	long long res = 1;
	while (b)
		if (b & 1)
			res = (res * 1ll * a) % m, --b;
		else
			a = (a * 1ll * a) % m, b >>= 1;
	return res;
}

bool miller_rabin(long long n) {
	long long b = 2;
	for (long long g; (g = gcd(n, b)) != 1; ++b)
		if (n > g)
			return false;
	long long p = 0, q = n - 1;
	while ((q & 1) == 0)
		++p, q >>= 1;
	long long rem = powmod(b, q, n);
	if (rem == 1 || rem == n - 1)
		return true;
	for (long long i = 1; i<p; ++i) {
		rem = (rem * 1ll * rem) % n;
		if (rem == n - 1)  return true;
	}
	return false;
}

long long jacobi(long long a, long long b)
{
	if (a == 0)  return 0;
	if (a == 1)  return 1;
	if (a < 0)
		if ((b & 2) == 0)
			return jacobi(-a, b);
		else
			return -jacobi(-a, b);
	long long a1 = a, e = 0;
	while ((a1 & 1) == 0)
		a1 >>= 1, ++e;
	long long s;
	if ((e & 1) == 0 || (b & 7) == 1 || (b & 7) == 7)
		s = 1;
	else
		s = -1;
	if ((b & 3) == 3 && (a1 & 3) == 3)
		s = -s;
	if (a1 == 1)
		return s;
	return s * jacobi(b % a1, a1);
}

bool bpsw(long long n) {
	if ((long long)sqrt(n + 0.0) * (long long)sqrt(n + 0.0) == n)  return false;
	long long dd = 5;
	for (;;) {
		long long g = gcd(n, abs(dd));
		if (1<g && g<n)  return false;
		if (jacobi(dd, n) == -1)  break;
		dd = dd<0 ? -dd + 2 : -dd - 2;
	}
	long long p = 1, q = (p*p - dd) / 4;
	long long d = n + 1, s = 0;
	while ((d & 1) == 0)
		++s, d >>= 1;
	long long u = 1, v = p, u2m = 1, v2m = p, qm = q, qm2 = q * 2, qkd = q;
	for (long long mask = 2; mask <= d; mask <<= 1) {
		u2m = (u2m * v2m) % n;
		v2m = (v2m * v2m) % n;
		while (v2m < qm2)   v2m += n;
		v2m -= qm2;
		qm = (qm * qm) % n;
		qm2 = qm * 2;
		if (d & mask) {
			long long t1 = (u2m * v) % n, t2 = (v2m * u) % n,
				t3 = (v2m * v) % n, t4 = (((u2m * u) % n) * dd) % n;
			u = t1 + t2;
			if (u & 1)  u += n;
			u = (u >> 1) % n;
			v = t3 + t4;
			if (v & 1)  v += n;
			v = (v >> 1) % n;
			qkd = (qkd * qm) % n;
		}
	}
	if (u == 0 || v == 0)  return true;
	long long qkd2 = qkd * 2;
	for (long long r = 1; r<s; ++r) {
		v = (v * v) % n - qkd2;
		if (v < 0)  v += n;
		if (v < 0)  v += n;
		if (v >= n)  v -= n;
		if (v >= n)  v -= n;
		if (v == 0)  return true;
		if (r < s - 1) {
			qkd = (qkd * 1ll * qkd) % n;
			qkd2 = qkd * 2;
		}
	}
	return false;
}

bool prime(long long n) { // эту функцию нужно вызывать для проверки на простоту
	for (long long i = 0; i<trivial_limit && p[i]<n; ++i)
		if (n % p[i] == 0)
			return false;
	if (p[trivial_limit - 1] * p[trivial_limit - 1] >= n)
		return true;
	if (!miller_rabin(n))
		return false;
	return bpsw(n);
}

void prime_init() { // вызвать до первого вызова prime() !
	for (long long i = 2, j = 0; j<trivial_limit; ++i) {
		bool pr = true;
		for (long long k = 2; k*k <= i; ++k)
			if (i % k == 0)
				pr = false;
		if (pr)
			p[j++] = i;
	}
}

long long isp(long long n) {
	for (long long d = 2; d * d <= n; d++) {
		if (n % d == 0) {
			return d;
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	set<long long> primes;

	cout << "Case #1:" << endl;
	long long rest = 50;

	prime_init();

	for (long long i = 2; i <= mx; i++) {
		if (prime(i)) {
			primes.insert(i);
		}
		else if (i % 2 == 1 && i > mx / 2) {
			long long d[sz];
			long long n = i;
			long long cur = sz - 1;
			while (n > 0) {
				d[cur--] = n % 2;
				n /= 2;
			}
			bool ok = true;
			vector<long long> num(11);
			for (long long pos = 3; pos <= 10; pos++) {
				long long n = 0;
				for (long long j = 0; j < sz; j++) {
					n *= pos;
					n += d[j];
				}
				if (prime(n)) {
					ok = false;
					break;
				}
			}
			if (ok) {
				for (long long pos = 2; pos <= 10; pos++) {
					long long n = 0;
					for (long long j = 0; j < sz; j++) {
						n *= pos;
						n += d[j];
					}
					num[pos] = isp(n);
					if (num[pos] == -1) {
						ok = false;
					}
				}
				if (!ok) {
					continue;
				}
				for (long long j = 0; j < sz; j++) {
					cout << d[j];
				}
				for (int pos = 2; pos <= 10; pos++) {
					cout << " " << num[pos];
				}
				cout << endl;
				rest--;
				if (rest == 0) {
					return  0;
				}
			}
		}
	}

	

	//system("pause");
	return 0;
}