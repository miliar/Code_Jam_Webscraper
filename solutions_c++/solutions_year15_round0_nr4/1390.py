#pragma ide diagnostic ignored "OCUnusedMacroInspection"
#pragma ide diagnostic ignored "UnusedImportStatement"
#define _USE_MATH_DEFINES

#define TASK A

#define forn(i, a, b) for (int i = (a); i < (b); i++)
#define INF int(1e9)
#define EPS 1e-9

#define int64 long long
#define uint64 unsigned long long
#define var auto
#define mp make_pair

#define A first
#define B second

#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>
#include <cstdlib>
#include <stack>
#include <list>
#include <ctime>

using namespace std;

#define d(p, e) { \
    auto d_macro_e = e; \
    auto d_macro_f = d_macro_e.first; \
    auto d_macro_s = d_macro_e.second; \
    auto d_macro_p = p; \
    *d_macro_p.first = d_macro_f; \
    *d_macro_p.second = d_macro_s; \
}

void solve(int t, int x, int w, int h) {
    d(mp(&w, &h), mp(min(w, h), max(w, h)));

    bool isRichard = false;

    isRichard = isRichard || (x >= 7 || (w * h) % x != 0);

    for (int a = 1; a <= x; a++) {
        for (int b = 1; b <= x; b++) {
            if (a + b - 1 == x) {
                isRichard = isRichard || (a > w && b > w);
                isRichard = isRichard || (a > w && a > h);
                isRichard = isRichard || (b > w && b > h);
            }
        }
    }

    isRichard = isRichard || (x == 6 && (w == 3 || h == 3));
    isRichard = isRichard || (x == 4 && w == 2 && h == 4);

    printf("Case #%d: %s\n", t, isRichard ? "RICHARD" : "GABRIEL");
}

int main(int argc, const char * argv[]) {
#ifdef MISTMAC
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    forn (i, 0, t) {
        int x, w, h;
        cin >> x >> w >> h;
        solve(i + 1, x, w, h);
    }
    return 0;
}