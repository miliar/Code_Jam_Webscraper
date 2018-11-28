#include <cstdio>
#include <set>
#include <algorithm>
#define infile "d.in"
#define outfile "d.out"
#define nMax 1013

using namespace std;

double a[nMax];
double b[nMax];
int n, x, y;

void read(double v[nMax], int n) {
    for (int i = 0; i < n; ++i) {
        scanf("%lf", &v[i]);
    }
}

void read() {
    scanf("%d\n", &n);
    read(a, n);
    read(b, n);
}

set <double> makeSet(double v[nMax]) {
    set <double> s;

    for (int i = 0; i < n; ++i) {
        s.insert(v[i]);
    }

    return s;
}

int solveWar() {

    int cnt = 0;
    set <double> h = makeSet(b);

    for (int i = n-1; i >= 0; --i) {
        set <double> ::iterator it = h.upper_bound(a[i]);
        if (it != h.end()) {
            h.erase(it);
        } else {
            ++cnt;
            h.erase(h.begin());
        }
    }

    return cnt;
}

int solveNotWar() {

    int cnt = 0;

    for (int loose = 0; loose < n; ++loose) {

        int crt = 0;
        set <double> h = makeSet(b);

        for (int i = 0; i < loose; ++i) {
            h.erase(*h.rbegin());
        }

        int le = loose, ri = n-1;

        while (le <= ri) {
            set <double> ::iterator it = h.upper_bound(a[ri]);
            if (a[le] > *h.begin()) {
                ++crt;
                h.erase(h.begin());
                le++;
            } else if (it == h.end()) {
                ++crt;
                h.erase(h.begin());
                ri--;
            } else {
                h.erase(*h.rbegin());
                le++;
            }
        }

        cnt = max(cnt, crt);
    }

    return cnt;
}

void print(double v[]) {

    for (int i = 0; i < n; ++i) {
        printf("%.3lf\n", v[i]);
    }
    printf("----\n");
}

void solve() {

    sort(a, a+n);
    sort(b, b+n);

    //print(a);
    //print(b);

    x = solveNotWar();
    y = solveWar();
}

void write(int t) {
    printf("Case #%d: %d %d\n", t, x, y);
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int t;
    scanf("%d\n", &t);

    for (int i = 0; i < t; ++i) {
        read();
        solve();
        write(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
