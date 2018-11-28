#include <bits/stdc++.h>
#define EPS 1e-11
using namespace std;

int t, n;
double v, x, r1, c1, r2, c2;

bool eq(double a, double b) {
    return abs(a-b)<EPS;
}

int main(void) {
    if (fopen("b-small.in","r")) {
        freopen("b-small.in","r",stdin);
        freopen("b-small.out","w",stdout);
    }
    cin >> t;
    for (int ii=1; ii<=t; ii++) {
        cin >> n >> v >> x;
        if (n==1) {
            cin >> r1 >> c1;
            if (!eq(c1,x)) {
                cout << "Case #" << ii << ": IMPOSSIBLE\n";
            }
            else {
                printf("Case #%d: %.9f\n", ii, v/r1);
            }
        }
        else {
            cin >> r1 >> c1 >> r2 >> c2;
            if (!eq(c2,c1)) {
                // det!=0
                if (c1>c2) {
                    swap(c1,c2);
                    swap(r1,r2);
                }
                double det=r1*r2*(c2-c1);
                double t1=v*r2*(c2-x)/det;
                double t2=-v*r1*(c1-x)/det;
                if (c2<x || c1>x) {
                    cout << "Case #" << ii << ": IMPOSSIBLE\n";
                }
                else {
                    printf("Case #%d: %.9f\n", ii, max(t1,t2));
                }
            }
            else {
                if (!eq(c1,x)) {
                    cout << "Case #" << ii << ": IMPOSSIBLE\n";
                }
                else {
                    printf("Case #%d: %.9f\n", ii, v/(r1+r2));
                }
            }
        }
    }
}
