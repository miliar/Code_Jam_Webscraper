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


void solve_case() {
    int i, j;
    double cost = getdouble();
    double add = getdouble();
    double goal = getdouble();
    double res = 1e100;
    double curr = 0.0;
    double prod = 2.0;
    for (; ; ) {
        res = min(res, curr + goal / prod);
        curr += cost / prod;
        prod += add;
        if (curr > res) break;
    }
    printf("%.7lf\n", res);
}

int main () {
    int tcc, tc = getint();
    for (tcc = 1; tcc <= tc; tcc++) {
        print_case(tcc);
        solve_case();
    }
    return 0;
}
