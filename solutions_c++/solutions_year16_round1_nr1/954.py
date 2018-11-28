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

typedef unsigned uint;
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

string doit(const string &s) {
    if (s == "")
        return "";
    int max_pos = max_element(all(s)) - s.begin();
    char max_ch = s[max_pos];
    int max_cnt = count(all(s), max_ch);

    string res = "";
    for (int i = max_pos + 1; i < sz(s); ++i) {
        if (s[i] != max_ch) {
            res += s[i];
        }
    }
    return string(max_cnt, max_ch) + doit(s.substr(0, max_pos)) + res;
}

void solve() {
    string s;
    cin >> s;
    cout << doit(s) << endl;
}

string bf(const string &s) {
    int n = sz(s);
    string best = "";
    for (int mask = 0; mask < (1 << n); ++mask) {
        string cur = "";
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                cur = string(1, s[i]) + cur;
            } else {
                cur += s[i];
            }
        }
        best = max(best, cur);
    }
    return best;
}

void stress() {
    for (int n = 1; n <= 15; ++n) {
        cerr << n << endl;
        for (int ch = 2; ch <= n; ++ch) {
            for (int t = 0; t < 1000; ++t) {
                string s = "";
                for (int i = 0; i < n; ++i)
                    s += rand() % ch + 'A';
                string ans = bf(s);
                string res = doit(s);
                if (ans != res) {
                    cerr << "FAIL" << endl;
                    cerr << s << endl;
                    cerr << "HAVE: " << res << endl;
                    cerr << "NEED: " << ans << endl;
                    exit(123);
                }
            }
        }
    }
    cerr << "PASSED" << endl;
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif

	//stress();

	int T;
	char buf[32];
    fgets(buf, sizeof buf, stdin);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
