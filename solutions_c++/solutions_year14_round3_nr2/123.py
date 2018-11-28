#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long lng;
typedef unsigned long long ulng;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, PII> PIII;
typedef pair<lng, PII> PLII;
#define FAIL ++*(int*)0
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define RR 151
#define X first
#define Y second
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "B"

const int MOD = INF + 7;

inline int mult(int x, int y) {
	return int(x * 1ll * y % MOD);
}

int n;
vector<string> a;
int ans;
int f[1000];

inline bool check(const string &s) {
	static int last[26];
	clr(last, -1);
	for (int i = 0; i < sz(s); ++i) {
		char ch = s[i] - 'a';
		if (last[ch] != -1 && last[ch] != i - 1)
			return false;
		last[ch] = i;
	}
	return true;
}

void doit() {
	for (int i = 0; i < n; ++i) {
		if (!check(a[i]))
			return;
	}

	vector<string> na;
	int mul = 1;
	for (int i = 0; i < n; ++i) {
		if (a[i] == "")
			continue;
		if (sz(a[i]) == 1) {
			na.push_back(a[i]);
			mul = mult(mul, f[count(all(a), a[i])]);
			replace(all(a), string(a[i]), string());
		} else {
			na.push_back(a[i]);
		}
	}
	a.swap(na);
	
	for (int i = 0; i < sz(a); ++i) {
		if (sz(a[i]) == 1) {
			int j = 0;
			for (; j < sz(a); ++j) {
				if (i == j || a[j] == "")
					continue;
				if (a[j].back() == a[i][0]) {
					break;
				}
				if (a[j].front()  == a[i][0]) {
					break;
				}
			}
			if (j == sz(a))
				continue;
			a[i] = "";
		}
	}
	na.clear();
	for (int i = 0; i < sz(a); ++i) {
		if (a[i] != "")
			na.push_back(a[i]);
	}
	a.swap(na);

	for (;;) {
		for (int i = 0; i < sz(a); ++i) {
			if (!check(a[i]))
				return;

			for (int j = i + 1; j < sz(a); ++j) {
				char used[26] = {0};
				for (int k = 0; k < sz(a[i]); ++k)
					used[a[i][k] - 'a'] = true;
				char any = -1;
				int common = 0;
				for (int k = 0; k < sz(a[j]); ++k) {
					if (used[a[j][k] - 'a']) {
						any = a[j][k];
						++common;
					}
				}
				if (common > 1)
					return;
				if (common == 0)
					continue;
				if (a[i].back() == any && a[j].front() == any)
					continue;
				if (a[i].front() == any && a[j].back() == any)
					continue;
				return;
			}
		}

		for (int i = 0; i < sz(a); ++i) {
			if (a[i] == "")
				continue;
			for (int j = 0; j < sz(a); ++j) {
				if (i == j || a[j] == "")
					continue;
				if (a[i].back() == a[j].front()) {
					a[i] += a[j];
					a[j] = "";
					break;
				}
			}
		}
		vector<string> na;
		for (int i = 0; i < sz(a); ++i) {
			if (a[i] != "") {
				a[i].erase(unique(all(a[i])), a[i].end());
				na.push_back(a[i]);
			}
		}
		if (a == na)
			break;
		a.swap(na);
	}
	for (int i = 0; i < sz(a); ++i) {
		if (!check(a[i]))
			return;
	}
	ans = f[sz(a)];
	ans = mult(ans, mul);
}

void solve() {
	cin >> n;
	a.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
		a[i].erase(unique(all(a[i])), a[i].end());
	}
	ans = 0;
	doit();
	printf("%d\n", ans);
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	f[0] = 1;
	for (int i = 1; i < 1000; ++i)
		f[i] = mult(f[i - 1], i);

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
