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

const int N = 1001;

int source[N];

int solve() {
    int mx = 0;

    forn (i, 0, N)
        if (source[i] > 0)
            mx = i;

    int answer = mx;

    forn (y, 1, answer + 1) {
        int x = 0;
        forn (i, y, N) {
            int t = (i - 1) / y;
            x += (source[i] * t);
        }

        answer = min(answer, x + y);
    }
    return answer;
}

int main(int argc, const char * argv[]) {
#ifdef MISTMAC
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    forn (i, 0, t) {
        int n;
        scanf("%d", &n);
        memset(source, 0, sizeof(int) * N);

        forn (j, 0, n) {
            int x;
            scanf("%d", &x);
            source[x]++;
        }

        printf("Case #%d: %d\n", i + 1, solve());
    }
    return 0;
}