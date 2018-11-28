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
//#include <ctime>
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
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<lng, lng> pii64;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define left huyleft
#define right huyright
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "C"
#define RR 151

const int MAXN = 10*1000*1001;

vector<lng> good;
lng pgood[40] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001};

inline lng rev(lng x) {
    lng res = 0;
    for (; x; x /= 10)
        res = res * 10 + x % 10;
    return res;
}

inline bool is_good(lng x) {
    return x == rev(x);
}

void precalc() {
    for (lng i = 1; i <= MAXN; ++i) {
        if (is_good(i) && is_good(i * i)) {
            good.push_back(i * i);
            cerr << i * i << ',';
        }
    }
    cout << endl;
    cerr << sz(good) << endl;
}

void solve () {
    lng l, r;
    cin >> l >> r;
    //r = upper_bound(all(good), r) - good.begin();
    //l = upper_bound(all(good), l) - good.begin();
    r = upper_bound(pgood, pgood + 40, r) - pgood;
    l = lower_bound(pgood, pgood + 40, l) - pgood - 1;
    cout << r - l - 1 << endl;
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
    freopen(TASK "-large-1.in", "r", stdin);
    freopen(TASK "-large-1.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    //precalc();

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
