#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
inline double getdouble() { unsigned int c; double x = 0, t = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getdouble(); if (c == '.') break; if (!~c) exit(0); } do { if (c == '.') t = 1; else { x = x * 10 + (c - '0'); if (t > 0) t *= 10; } } while (((c = gc()) - '0') < 10 or c == '.'); if (t > 0) return x / t; return x; }

template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

int n;
double vw;
double tw;
double rates[111];
double temps[111];

void solve_case() {
    int i, j;
    n = getint();
    vw = getdouble();
    tw = getdouble();
    for (i = 0; i < n; i++) {
        rates[i] = getdouble();
        temps[i] = getdouble();
    }
    double res = -1;
    if (n == 1) {
        if (temps[0] == tw) {
            res = vw / rates[0];
        } else {
            res = -1;
        }
    } else {
        if (temps[1] < temps[0]) {
            swap(temps[0], temps[1]);
            swap(rates[0], rates[1]);
        }
        if (temps[0] == temps[1] && temps[0] == tw) {
            res = vw / (rates[0] + rates[1]);
        } else if (temps[0] == tw) {
            res = vw / (rates[0]);
        } else if (temps[1] * 1000 == 1000 * tw) {
            res = vw / (rates[1]);
        } else if (temps[0] < tw && tw < temps[1]) {
            double v0 = (tw * vw - temps[1] * vw) / (temps[0] - temps[1]);
            double v1 = vw - v0;
            res = max(v0 / rates[0], v1 / rates[1]);
        }
    }
    if (res < 0) {
        puts("IMPOSSIBLE");
    } else {
        printf("%.10lf\n", res);
    }
    return;
}

int main () {
    int test_count, test_case = getint();
    for (test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
