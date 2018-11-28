#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define mp make_pair
#define eps 1e-9

using namespace std;

inline bool eq(double a, double b) {
    return (a > b-eps && a < b+eps);
}

typedef long long ll;
int n;
double v, x;
vector<double> r, c;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, NT;
    cin>>NT;
    int i, j, n, m;
    for(T=1; T<=NT; ++T) {
        cin>>n>>v>>x;
        r.clear();
        c.clear();
        r.resize(n);
        c.resize(n);
        for(i=0; i<n; ++i) {
            cin>>r[i]>>c[i];
        }
        double res=0;
        if (n == 2 && eq(c[0], c[1])) {
            n = 1;
            r[0] += r[1];
        }
        if (n == 1) {
            if (eq(c[0], x)) {
                res = v / r[0];
                printf("Case #%d: %.9f\n", T, res);
            } else {
                printf("Case #%d: IMPOSSIBLE\n", T);
            }
            continue;
        }
        if (n == 2) {
            if (c[0] > c[1]) {
                swap(c[0], c[1]);
                swap(r[0], r[1]);
            }
            if (eq(x, c[0])) {
                res = v / r[0];
                printf("Case #%d: %.9f\n", T, res);
                continue;
            } else if (eq(x, c[1])) {
                res = v / r[1];
                printf("Case #%d: %.9f\n", T, res);
                continue;
            } else if (c[0] < x && x < c[1]) {
                double part0 = (c[1]-x) / (c[1]-c[0]);
                double t = (part0*v) / r[0];
                res = t;
                double part1 = 1-part0;
                t = (part1*v) / r[1];
                res = max(res, t);
                printf("Case #%d: %.9f\n", T, res);
                continue;
            } else {
                printf("Case #%d: IMPOSSIBLE\n", T);
                continue;
            }
        }
    }
    return 0;
}

