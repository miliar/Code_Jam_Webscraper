#ifdef _MSC_VER
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <iostream>
#include <fstream>
#include <cassert>
#include <ctime>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <list>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <limits>
#include <cstring>
using namespace std;

typedef long long li;
typedef unsigned long long uint64;
typedef unsigned int uint;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef long double ld;
typedef pair<int,int> pt;


#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n - 1); i >= 0; i--)
#define pb push_back
#define mp make_pair
#define matrix(T,n,m,v) vector<vector<T> >(n, vector<T>(m, v))
#define ft first
#define sc second
#define x first
#define y second
#define all(x) (x).begin(), (x).end()
#define sz(x) (x).size()

template<class T> T sqr(const T& x) { return x * x; }
template<class T> T abs(const T& x) { return x < 0 ? -x : x; }

template<class T, class P>
ostream& operator << (ostream& out, std::pair<T, P> p) {
	return (out << '(' << p.first << ' ' << p.second << ')');
}

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-8;
const ld PI = 3.1415926535897932384626433832795;

ld c, f, x;

bool read() {
	cin >> c >> f >> x;
	return true;
}

ld calc(int cnt) {
	ld t = 0.0;
	ld p = 2.0;
	forn (i, cnt) {
		t += c / p;
		p += f;
	}
	t += x / p;
	return t;
}

void solve(int test) {
	int l = 0;
	int r = 100 * 1000;

	while (r - l > 10) {
		int ml = (l + r) / 2 - 1;
		int mr = (l + r) / 2 + 1;
		ld vl = calc(ml);
		ld vr = calc(mr);
		if (vl > vr) {
			l = ml;
		} else {
			r = mr;
		}
	}

	ld ans = 1e18;
	for (int i = max(0, l - 10); i < r + 10; i++) {
//		cerr << i << ' ' << calc(i) << endl;
		ans = min(ans, calc(i));
	}

	printf("Case #%d: %.10lf\n", test, double(ans));
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testCnt;
	cin >> testCnt;

	forn (test, testCnt) {
		read();
		solve(test + 1);
	}

	cerr << clock() << endl;
	
    return 0;
}