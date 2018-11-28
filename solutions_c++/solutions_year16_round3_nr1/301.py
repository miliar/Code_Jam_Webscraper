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

string doit(vector<int> cnts) {
    int total = accumulate(all(cnts), 0);
    //int mn = *min_element(all(cnts));
    priority_queue<pii> pq;
    forv(i, cnts)
        pq.push(mp(cnts[i], i));
    string res = "";
    while (!pq.empty()) {
        if (sz(res)) res += ' ';
        pii a = pq.top(); pq.pop();
        if (a.X * 2 > total) exit(66);
        --a.X;
        --total;
        res += a.Y + 'A';
        if (sz(pq)==1 && pq.top().X == a.X + 1) {
            pii a = pq.top(); pq.pop();
            //if (a.X * 2 > total) exit(66);
            --a.X;
            --total;
            res += a.Y + 'A';
            if (a.X) pq.push(a);
        }/* else if (!pq.empty() && pq.top().X < a.X) {
            --a.X;
            --total;
            res += a.Y + 'A';
        }*/
        if (a.X) pq.push(a);
    }
    return res;
}

void solve() {
    int n;
    cin >> n;
    vector<int> c(n);
    for (int &x : c)
        cin >> x;
    cout << doit(c) << endl;
}

void stress() {
    for (int n = 3; n <= 10; ++n) {
        cerr << n << endl;
        for (int t = 0; t < 10000; ++t) {
            vector<int> c;
            for (;;) {
                c.clear();
                forn(i, n)
                    c.push_back(rand() % 100 + 1);
                int total = accumulate(all(c), 0);
                forv(i, c)
                    if (c[i] * 2 > total) { c.clear(); break; }
                if (sz(c))break;
            }
            doit(c);
        }
    }
    cerr << "PASSED" << endl;
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
