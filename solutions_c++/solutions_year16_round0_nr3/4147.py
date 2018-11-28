#include <iostream>
#include <cassert>
#include <fstream>
#include <sstream>
#include <math.h>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <time.h>
#include <stdio.h>
#include <direct.h>
#include <windows.h>
#include <mutex>
#include <process.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define POW(n) (n*n)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned char CharactorID;
typedef unsigned char Space;
typedef unsigned char sPos;
typedef short Pos;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;
const int N = (80000000-1);
bool arr[N];

class Radix {
private:
	const char* s;
	int a[128];
public:
	Radix(const char* s = "0123456789ABCDEF") : s(s) {
		int i;
		for (i = 0; s[i]; ++i)
			a[(int)s[i]] = i;
	}
	std::string to(long long p, int q) {
		int i;
		if (!p)
			return "0";
		char t[64] = {};
		for (i = 62; p; --i) {
			t[i] = s[p % q];
			p /= q;
		}
		return std::string(t + i + 1);
	}
	std::string to(const std::string& t, int p, int q) {
		return to(to(t, p), q);
	}
	long long to(const std::string& t, int p) {
		int i;
		long long sm = a[(int)t[0]];
		for (i = 1; i < (int)t.length(); ++i)
			sm = sm * p + a[(int)t[i]];
		return sm;
	}
};

Radix r;

ll cPow(int r,int l) {
	ll ret = 1;
	REP(i,l) {
		ret *= r;
	}
	return ret;
}

ll hex(string str, int rad) {
	ll ret = 0;

	int len = str.length();
	for (int i = 0; i < len; ++i) {
		int k = len - i - 1;

		if (str[i] == '1') {
			ret += cPow(rad,k);
		}
	}
	return ret;
}

void Eratosthenes() {
	for (int i = 1; i < N; i++) {
		arr[i] = 1;
	}
	for (int i = 2; i < sqrt(N); i++) {
		if (arr[i]) {
			for (int j = 0; i * (j + 2) < N; j++) {
				arr[i *(j + 2)] = 0;
			}
		}
	}
}

bool chk(bool list[10]) {
	REP(i, 10) {
		if (!list[i]) {
			return false;
		}
	}
	return true;
}

void solve(const int N , const int J) {
	ll base = 0x1 << (N-1);
	ll end = 0x1 << (N);

	int j = 0;

	for (ll n = base; n < end; ++n) {
		if (n % 2 == 0)continue;
		bool isOK = false;
		string st2 = r.to(n, 2);
		string str = st2;

		int b = 2;
		for (; b <= 10; ++b) {
			ll _n = hex(st2, b);
			ll sosuu = -1;
			bool flag = false;

			for (ll c = 2; c < min(_n/2, 80000000-1); ++c) {
				if (!arr[c])continue;
				if (_n % c == 0) {
					sosuu = _n / c;
					flag = true;
					break;
				}
			}
			if (!flag)break;
			str += " " + to_string(sosuu);
		}
		if (b != 11)continue;
		cout << str << endl;
		j++;
		if (j == J)return;
	}

	int z = 0;
}

int main() {
	Eratosthenes();
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int N,J;
		cin >> N >> J;
		cout << "Case #" << t << ":" << endl;
		solve(N,J);
	}

	return 0;
}