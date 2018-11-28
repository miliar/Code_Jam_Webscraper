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
typedef pair<int, int> pii;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, pii> PIII;
typedef pair<lng, pii> PLII;
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
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "A"

int n, R, P, S;

string doit() {
    map<char, string> win;
    win['P'] = "PR";
    win['R'] = "RS";
    win['S'] = "PS";
    string ans = "Z";
    for (char start : { 'R', 'P', 'S' }) {
        string s;
        s += start;
        forn(depth, n) {
            string next;
            for (char ch : s) {
                next += win[ch];
            }
            swap(s, next);
        }
        if (count(all(s), 'P') != P) continue;
        if (count(all(s), 'R') != R) continue;
        if (count(all(s), 'S') != S) continue;
        forn(depth, n) {
            for (int i = 0; i + (1 << depth) < sz(s); i += 1 << (depth + 1)) {
                if (s.substr(i, 1 << depth) > s.substr(i + (1 << depth), 1 << depth)) {
                    string t = s.substr(i, 1 << depth);
                    for (int j = i; j < i + (1 << depth); ++j) {
                        s[j] = s[j + (1 << depth)];
                    }
                    for (int j = i; j < i + (1 << depth); ++j) {
                        s[j + (1 << depth)] = t[j - i];
                    }
                }
            }
        }
        ans = min(ans, s);
    }
    if (ans == "Z") ans = "IMPOSSIBLE";
    return ans;
}

void solve() {
    cin >> n >> R >> P >> S;
    cout << doit() << endl;
}

//void stress() {
//    for (int n = 3; n <= 10; ++n) {
//        for (int t = 0; t < 1000; ++t) {
//            if (ans != res) {
//                cerr << "FAIL" << endl;
//                cerr << "NEED: " << ans << endl;
//                cerr << "HAVE: " << res << endl;
//                exit(66);
//            }
//        }
//    }
//    cerr << "PASSED" << endl;
//}

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
