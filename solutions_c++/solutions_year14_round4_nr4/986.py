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

#define TASK "D"

struct trie {
	struct node {
		int next[26];
		node() {
			clr(next, -1);
		}
	};

	vector<node> a;

	trie() {
		a.push_back(node());
	}

	void add(const string &s) {
		int v = 0;
		for (int i = 0; i < sz(s); ++i) {
			int ch = s[i] - 'A';
			if (a[v].next[ch] == -1) {
				a[v].next[ch] = sz(a);
				a.push_back(node());
			}
			v = a[v].next[ch];
		}
	}
};

int n, m;
vector<string> a;
int ids[10];

int best;
int best_cnt;

void rec(int x) {
	if (x == m) {
		if (sz(set<int>(ids, ids + m)) < n)
			return;
		vector<trie> t(n);
		for (int i = 0; i < m; ++i) {
			t[ids[i]].add(a[i]);
		}
		int cur = 0;
		for (int i = 0; i < n; ++i)
			cur += sz(t[i].a);
		if (cur > best) {
			best = cur;
			best_cnt = 0;
		}
		if (cur == best)
			++best_cnt;
		return;
	}
	for (int i = 0; i < n; ++i) {
		ids[x] = i;
		rec(x + 1);
	}
}

void solve() {
	cin >> m >> n;
	a.resize(m);
	for (int i = 0; i < m; ++i)
		cin >> a[i];
	best = 0;
	rec(0);
	cout << best << ' ' << best_cnt << endl;
}

//#define DEBUG
#define SMALL
//#define LARGE

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

	//stress();

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
