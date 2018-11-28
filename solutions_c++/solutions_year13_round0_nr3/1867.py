#include <cstdio>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ctime>

#include <iostream>
#include <fstream>
#include <sstream>

#include <algorithm>
#include <utility>

#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <unordered_set>

using namespace std;

#define fi(i, n) for (int i = 0; i < (n); ++i)
#define fv(i, v) fi (i, (v).size())
#define fab(i, a, b) for (int i = (a); i <= (b); ++i)
#define fba(i, b, a) for (int i = (b); i >= (a); --i)

#define V vector
#define VI vector<int>
#define VS vector<string>
#define uint unsigned int
#define uchar unsigned char
#define LL long long
#define uLL unsigned LL

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz size()

uLL fact(int n, uLL mod) { return n ? n * fact(n - 1, mod) % mod : 1; }
uLL gcd(uLL a, uLL b) { return a ? gcd(b % a, b) : b; }
uLL qpow(uLL a, uLL b, uLL mod) { if (!b) return 1; if (b % 2) return a * qpow(a, b - 1, mod) % mod; else {uLL t = qpow(a, b / 2, mod); return t * t % mod; }}
/*
class BigInt {
	static const uLL mod = 1000000000;
	static const uLL mod_len = 9;
	vector<uLL> data;
public:
	BigInt() {};
	BigInt(const vector<uLL> &x) : data(x) {};
	BigInt(BigInt &x) : data(x.data) {};
	BigInt(string &z) {
		uLL buf = 0;
		for (auto it = z.rbegin(); it != z.rend(); ++it) {

	};

	BigInt operator * (BigInt &a) {
		vector<uLL> res;
		res.reserve(a.data.size() + data.size());
		uLL o = 0;
		int zeros = 0;
		fi(i, a.data.size() + data.size()) {
			fi(j, i) {
				int k = i - j;
				if (j < a.data.size() && k < data.size()) {
					o += a.data[j] * data[k];
				}
			}
			if (o != 0) {
				while (zeros) {
					--zeros;
					res.pb(0);
				}
				res.pb(o % mod);
				o /= mod;
			} else {
				++zeros;
			}
		}
		return BigInt(res);
	}

	operator string() {
		string res;
		int zeros = 0;
		fv(i, data) {
			int t = data[i];
			fi(j, mod_len) {
				if (t != 0) {
					while (zeros) {
						--zeros;
						res.pb('0');
					}
					res.pb('0' + t % 10);
					t /= 10;
				} else {
					++zeros;
				}
			}
		}
		return res;
	}

	void addToOddPal() {

	}
}
*/


vector<uLL> pc;

uLL numLen10(uLL x) {
	if (x < 1ULL) return 1;
	if (x < 10ULL) return 10;
	if (x < 100ULL) return 100;
	if (x < 1000ULL) return 1000;
	if (x < 10000ULL) return 10000;
	if (x < 100000ULL) return 100000;
	if (x < 1000000ULL) return 1000000;
	if (x < 10000000ULL) return 10000000;
	if (x < 100000000ULL) return 100000000;
	if (x < 1000000000ULL) return 1000000000;
	if (x < 10000000000ULL) return 10000000000;
	if (x < 100000000000ULL) return 100000000000;
	if (x < 1000000000000ULL) return 1000000000000;
	if (x < 10000000000000ULL) return 10000000000000;
	if (x < 100000000000000ULL) return 100000000000000;
	if (x < 1000000000000000ULL) return 1000000000000000;
	if (x < 10000000000000000ULL) return 10000000000000000;
}

uLL reverseInt(uLL x) {
	uLL res = 0;
	do {
		res = 10 * res + x % 10;
	} while (x /= 10);
	return res;
}

uLL mirror1(uLL x) {
	return x * numLen10(x) + reverseInt(x);
}

uLL mirror2(uLL x) {
	return (x / 10) * numLen10(x) + reverseInt(x);
}

inline bool isPal(uLL x) {
	return x == reverseInt(x);
}

void preCalc() {
	unordered_set<uLL> res;
	for (int i = 0; i < 10000; ++i) {
		uLL x = mirror1(i);
		uLL y = mirror2(i);
		if (isPal(x * x)) {
			res.insert(x * x);
		}
		if (isPal(y * y)) {
			res.insert(y * y);
		}
	}
	for (auto it = res.begin(); it != res.end(); ++it) {
		pc.pb(*it);
	}
	sort(all(pc));
}

void solve_the_problem() {
	uLL a, b;
	cin >> a >> b;
	++b;
	int h, l, m;
	int lb, rb;
	l = 0; h = pc.size();
	while (h - l > 1) {
		m = (h + l) / 2;
		if (pc[m] < a) {
			l = m;
		} else {
			h = m;
		}
	}
	lb = h;
	l = 0; h = pc.size();
	while (h - l > 1) {
		m = (h + l) / 2;
		if (pc[m] < b) {
			l = m;
		} else {
			h = m;
		}
	}
	rb = h;
	cout << rb - lb;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	preCalc();
	fab(i, 1, t) {
		//cerr << "Test #" << i << ":" << endl;
		cout << "Case #" << i << ": ";
		solve_the_problem();
		cout << endl;
	}
	return 0;
}
