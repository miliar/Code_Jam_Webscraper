#include <algorithm>
#include <bitset>
#include <cctype>
#include <cfloat>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>

using namespace std;
typedef long long ll;

void print_case(int tc) { printf("Case #%d: ", tc); }
#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
double getdouble() { unsigned int c; double x = 0, t = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getdouble(); if (c == '.') break; if (!~c) exit(0); } do { if (c == '.') t = 1; else { x = x * 10 + (c - '0'); if (t > 0) t *= 10; } } while (((c = gc()) - '0') < 10 or c == '.'); if (t > 0) return x / t; return x; }

const int inf = 1 << 28;
int n;
int aas[1024], bbs[1024];
int as[1024], bs[1024];

void solve_case() {
    int i, j, resa = 0, resb = 0;
    n = getint();
    for (i = 0; i < n; i++) as[i] = (int)(getdouble() * 1000000);
    for (i = 0; i < n; i++) bs[i] = (int)(getdouble() * 1000000);
    sort(as, as + n), sort(bs, bs + n);
    for (i = 0; i < n; i++) aas[i] = as[i], bbs[i] = bs[i];
    int bp = 0;
    for (i = 0; i < n; i++) {
        int k = inf;
        for (; bp < n; bp++) if (as[i] < bs[bp]) { k = min(bs[bp], k); break; }
        bp++;
        if (k == inf) resb++;
    }
    for (i = 0; i < n; i++) as[i] = aas[i], bs[i] = bbs[i];
    int bend = n;
    bp = 0;
    for (i = 0; i < n; i++) {
        if (as[i] > bs[bp]) {
            bp++, resa++;
        }
    }

    cout << resa << ' ' << resb << endl;
}

int main () {
    int tcc, tc = getint();
    for (tcc = 1; tcc <= tc; tcc++) {
        print_case(tcc);
        solve_case();
    }
    return 0;
}
