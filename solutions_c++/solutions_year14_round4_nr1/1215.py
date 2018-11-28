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

#define TASK "A"

int n, X;
int s[10000];
int dp[10010][10010];

int rec(int x, int last) {
	if (x > last)
		return 0;
	int &res = dp[x][last];
	if (res != -1)
		return res;
	res = rec(x + 1, last) + 1;
	if (x < last) {
		int add = 0;
		for (; last > x && s[last] + s[x] > X; --last)
			++add;
		if (x < last)
			res = min(res, rec(x + 1, last - 1) + add + 1);
	}
	return res;
}

char used[10];
int best_ans;
int ans;

void rec2(int x) {
	if (x >= n) {
		best_ans = min(best_ans, ans);
		return;
	}
	if (used[x])
		rec2(x + 1);
	else {
		++ans;
		rec2(x + 1);
		
		for (int i = x + 1; i < n; ++i) {
			if (!used[i] && s[x] + s[i] <= X) {
				used[i] = true;
				rec2(x + 1);
				used[i] = false;
			}
		}

		--ans;
	}
}

void solve() {
	cin >> n >> X;
	for (int i = 0; i < n; ++i)
		cin >> s[i];
	sort(s, s + n);
	clr(dp, -1);
	printf("%d\n", rec(0, n - 1));
}

void stress() {
	for (n = 1; n <= 10; ++n) {
		for (X = 10; X <= 100; X += 90) {
			cerr << n << ' ' << X << endl;
			for (int ttt = 0; ttt < 10000; ++ttt) {
				for (int i = 0; i < n; ++i)
					s[i] = rand() % (X - 1) + 1;
				ans = 0;
				best_ans = INF;
				rec2(0);
				ans = best_ans;
				sort(s, s + n);
				clr(dp, -1);
				int res = rec(0, n - 1);
				if (res != ans) {
					cerr << "FAIL" << endl;
					cerr << "NEED: " << ans << endl;
					cerr << "HAVE: " << res << endl;
					cout << n << ' ' << X << endl;
					for (int i = 0; i < n; ++i)
						cout << s[i] << ' ';
					cout << endl;
					exit(23);
				}
			}
		}
	}
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt1.in", "r", stdin);
    freopen(TASK "-small-attempt1.out", "w", stdout);
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
