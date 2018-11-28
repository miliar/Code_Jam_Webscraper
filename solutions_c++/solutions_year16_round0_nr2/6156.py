#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:640000000")

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn1(i, n) for(int i = 1; i <= (int)(n); i++)
#define forr(i, l, r) for(int i = int(l); i <= int(r); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define y1 __y1
#define sqr(x) ((x) * (x))

typedef long long li;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long uli;
typedef pair<int, int> pt;

inline void read(int&);
inline void read(li&);
inline void read(ld&);
inline void read(char&);
inline void read(string&);
template <typename T1, typename T2> inline void read(T1&, T2&);
template <typename T1, typename T2, typename T3> inline void read(T1&, T2&, T3&);
template <typename T1, typename T2, typename T3, typename T4> inline void read(T1&, T2&, T3&, T4&);

inline void read(string &s) {
	static char buf[int(1e6) + 10];
	assert(scanf("%s", buf) == 1);
	s = string(buf);
	return;
}

const int INF = (int)(1e9);
const li INF64 = (li)(INF)* (li)(INF);
const ld eps = 1e-9;
const ld pi = ld(3.1415926535897932384626433832795);

inline bool in(int i, int j, int n, int m) {
	return i >= 1 && i <= n && j >= 1 && j <= m;
}

inline int myrand() {
	return (rand() ^ (rand() << 15));
}

inline li randL() {
	return myrand() * 1LL * myrand() + myrand();
}

const int dx[] = { 0, -1, 1, 0 };
const int dy[] = { -1, 0, 0, 1 };

const int N = 11;

string s;
int n;

inline void gen() {
	return;
}

inline bool read() {
	if (!(cin >> s)) return false;
	return true;
}

bool dp[2 * N][(1 << N)];
bool used[(1 << N)];

inline void solve() {
	forn(i, (1 << N)) used[i] = false;
	forn(i, 2 * N) forn(mask, (1 << N)) dp[i][mask] = false;
	int initMask = 0;
	n = sz(s);
	forn(i, n) if (s[i] == '+') initMask |= (1 << i);
	dp[0][initMask] = true;
	forn(i, 2 * N - 1) forn(mask, (1 << n)) {
		if (!dp[i][mask]) continue;
		if (used[mask]) continue;
		used[mask] = true;
		//cerr << "i mask == " << i << ' ' << mask << endl;
		//string ss = "";
		string t = "";
		forn(j, n) t += ((mask & (1 << j)) ? '+' : '-');
		//cerr << "T == " << t << endl;
		for (int j = 0; j < n; j++) {
			string ss = "";
			for(int k = 0; k <= j; k++) ss += t[k];
			reverse(all(ss));
			forn(k, sz(ss)) if (ss[k] == '+') ss[k] = '-'; else ss[k] = '+';
			for (int k = j + 1; k < n; k++) ss += t[k];
			int nmask = 0;
			forn(k, n) if (ss[k] == '+') nmask |= (1 << k);
			//cerr << "j ss == " << j << ' ' << ss << endl;
			dp[i + 1][nmask] = true;
		}
	}

	forn(i, 2 * N) if (dp[i][(1 << n) - 1]) {
		cout << i << endl;
		return;
	}

	assert(false);
	return;
}

int main() {

#ifdef _DEBUG
	assert(freopen("input.txt", "rt", stdin));
	assert(freopen("output.txt", "wt", stdout));
#else
#endif

	cout << setprecision(10) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));

	int T = 1;
	assert(scanf("%d", &T) == 1);

	forn(i, T) {
		cerr << "TEST == " << i + 1 << endl;
		cout << "Case #" << i + 1 << ": ";
		assert(read());
		solve();
	}


#ifdef _DEBUG
	cerr << "TIME == " << clock() << " ms" << endl;
#endif
	return 0;
}