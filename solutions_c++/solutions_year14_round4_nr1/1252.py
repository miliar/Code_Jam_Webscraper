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
int getc_str(char str[]) { unsigned int c, n = 0; while ((c = gc()) <= ' '); if (!~c) exit(0); do { str[n++] = c; } while ((c = gc()) > ' ' ); str[n] = '\0'; return n; }

typedef pair<int, int> Segt;
const Segt segu = make_pair(-1, 0);
int segn = 2;
Segt seg[11000 * 5];

int gen_size(int n) { while (segn <= n) segn <<= 1; return segn; }

Segt range(int a, int b) {
    Segt res = segu;
    for (a += segn, b += segn; a <= b; a >>= 1, b >>= 1) {
        if ( a & 1) res = max(res, seg[a++]);
        if (~b & 1) res = max(res, seg[b--]);
    }
    return res;
}

void up(int i, Segt v) {
    seg[i += segn] = v;
    for (i >>= 1; i; i >>= 1) {
        seg[i] = max(seg[i << 1], seg[i << 1 | 1]);
    }
}


template<class S, class T> ostream &operator<<(ostream& os, const pair<S, T>& a) {
    os << "(" << a.first << ' ' << a.second << ")";
    return os;
}

int n, x;
int in[11000];

void solve_case() {
    int i, j;
    n = getint();
    x = getint();

    multiset<int> st;
    for (i = 0; i < n; i++) in[i] = getint(), st.insert(in[i]);

    gen_size(x + 1);
    for (i = 0; i < segn * 2; i++) seg[i] = segu;


    for (i = 0; i < n; i++) {
        int d = in[i];
        seg[segn + d].first = d;
        seg[segn + d].second++;
    }
    for (i = segn - 1; i; --i) {
        seg[i] = max(seg[i * 2], seg[i * 2 + 1]);
    }

    int res = 0;

    for (; ; ) {
        pair<int, int> p = range(0, x + 1);
        if (p.first < 0) break;
        p.second--;
        int rest = x - p.first;
        int ppos = p.first;
        if (p.second == 0) p.first = -1;
        up(ppos, p);
        pair<int, int> q = range(1, rest);
        res++;
        if (q.first < 0) {
        } else {
            q.second--;
            int qpos = q.first;
            if (q.second == 0) q.first = -1;
            up(qpos, q);
        }
    }
    cout << res << endl;
}

int main () {
    int tcc, tc = getint();
    for (tcc = 1; tcc <= tc; tcc++) {
        print_case(tcc);
        solve_case();
    }
    return 0;
}
