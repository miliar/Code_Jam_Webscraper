/*
    Author: Nikolay Kuznetsov
    Dedicated to my Love, Kristina Dmitrashko
*/
#ifdef NALP_PROJECT
#pragma hdrstop
#else
#define _SECURE_SCL 0
#endif

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <memory.h>

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define y1 YYY1
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> inline T Abs(T x) { return (x >= 0) ? x : -x; }
template<typename T> inline T sqr(T x) { return x * x; }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int bit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 nextInt64() { int64 x; if (scanf("%I64d", &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 100100;

set<vector<int> > st;
int n, m, k, a[MAXN];

bool can(const vector<int> &a, int x, int v) {
	if (x == 1) return true;
	if (v == (int)a.size()) return false;

	if (can(a, x, v + 1))
		return true;

	if (x % a[v] == 0 && can(a, x / a[v], v + 1))
		return true;

	return false;
}

void gen(int v, int last) {
	if (v == n) {
		st.insert(vector<int>(a, a + n));
		return;
	}

	for(int i = last; i <= m; i++) {
		a[v] = i;
		gen(v + 1, i);
	}
}

void solve() {
	int tests = nextInt();
	n = nextInt();
	m = nextInt();
	k = nextInt();

	st.clear();
	gen(0, 2);

	forn(test, tests) {
		forn(i, k)
			a[i] = nextInt();

		vector<int> ans(n, 2);
		for(set<vector<int> >::iterator i = st.begin(); i != st.end(); i++) {
			bool ok = true;
			forn(j, k)
				if (!can(*i, a[j], 0)) {
					ok = false;
					break;
				}

			if (ok)
				ans = *i;
		}

		forn(i, n)
			cout << ans[i];
		cout << endl;
	}
}

int main() {
#ifdef NALP_PROJECT
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#else
#endif

	srand(time(0));
	int tests = nextInt();
	forn(test, tests) {
		cerr << "Case #" << test + 1 << endl;
		cout << "Case #" << test + 1 << ":\n";
		solve();
	}

	return 0;
}
