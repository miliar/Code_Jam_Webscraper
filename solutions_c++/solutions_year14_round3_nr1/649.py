#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <string>

using namespace std;

// --------------------- Template ---------------------------------------------

#define FOR(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define FORN(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T, class IT>
inline void PRINT(IT i1, IT i2) {
    cout << '['; copy(i1, i2, ostream_iterator<T>(cout, ", ")); cout << "]\n";
}

#if defined(M_H_HOME) && (0)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

size_t count_ones(unsigned long long x) {
	size_t res = 0;
	while (x) { 
		x = x & (x - 1);
		++res;
	}
	return res;
}

ll gcd(ll a, ll b) {
	while (b != 0) {
		ll tmp = b;
		b = a % b;
		a = tmp;
	}
	return a;
}

int solve(ll num, ll den) {
	int result = 0;
	while (num != den) {
		den >>= 1;
		num = min(num, den);
		++result;
	}
	return result;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("a.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		string inp;
		cin >> inp;
		int p = 0;
		while (p < inp.size() && inp[p] != '/') ++p;
		if (p >= inp.size() - 1 || p == 0) {
			cerr << "tc = " << tc << '\n';
			continue;
		}
		ll num = stoll(inp.substr(0, p));
		ll den = stoll(inp.substr(p + 1));
		ll cd = gcd(num, den);
		num /= cd;
		den /= cd;
		if (count_ones(den) != 1 || num > den) {
			cout << "Case #" << tc << ": impossible\n";
			continue;
		}
		cout << "Case #" << tc << ": " << solve(num, den) << '\n';
	}

    return 0;
}
