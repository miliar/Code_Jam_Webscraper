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

int n;
vector<ld> a, b;

void solve() {
	cin >> n;
	a.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	b.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> b[i];
	}
	sort(all(a));
	sort(all(b));
	int ans2 = 0;
	for (int l = 0, r = 0; l < n; ++l) {
		for (; r < n && b[r] < a[l]; ++r) ;
		if (r < n)
			++ans2, ++r;
	}
	ans2 = n - ans2;

	int ans1 = 0;
	multiset<ld> pq(all(b));
	for (int i = 0; i < n; ++i) {
		if (a[i] < *pq.begin()) {
			pq.erase(pq.find(*pq.rbegin()));
		} else {
			++ans1;
			pq.erase(pq.begin());
		}
	}
	printf("%d %d\n", ans1, ans2);
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
