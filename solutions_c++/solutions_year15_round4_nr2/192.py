#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

int n; long double  R, C;
long double r[100], c[100];
const long double eps = 1e-11;
int cmp(long double x, long double y) {
    if (abs(x - y) < eps)
        return 0;
    if (x<y) return -1;
    else return 1;
}

bool ok(long double T) {
    long double S = 0, U = 0, P = 0;
    long double F = 0;
    for (int i = 1; i <= n; i++) {
        if (cmp(S + r[i] * T , R) <= 0) {
            S += r[i]*T;
            F += r[i]*c[i]*T;
        } else {
            long double t = (R - S) / r[i];
            S = R;
            F += r[i]*c[i]*t;
            break;
        }
    }
    if (cmp(S,R) < 0) return false;
    U = F / R;
    F = S = 0;
    for (int i = n; i >= 1; i--) {
        if (cmp(S + r[i] * T , R) <= 0) {
            S += r[i]*T;
            F += r[i]*c[i]*T;
        } else {
            long double t = (R - S) / r[i];
            S = R;
            F += r[i]*c[i]*t;
            break;
        }
    }
    P = F / R;
    if (cmp(U,C) <= 0 && cmp(C, P) <= 0) return true;
    else return false;
}

void sort(){
    for (int i = 1; i <= n;i++)
    for (int j=i+1;j<=n;j++)
        if (c[j]<c[i]){
            swap(c[i],c[j]);
            swap(r[i],r[j]);
        }
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin >> T;

    for (int o = 1; o <= T; o++) {
        cin >> n >> R >> C;
        int xx=0,yy=0,zz=0;
        for (int i = 1; i <= n; i++) {
            cin >> r[i] >> c[i];
            int k = cmp(c[i],C);
            if (k==0)zz++;
            if (k==-1)xx++;
            if (k==1)yy++;
        }
        sort();
        if (zz==0 && (xx==0||yy==0)) {
            printf("Case #%d: IMPOSSIBLE\n",o);
            continue;
        }
        long double l = 0, r = 99900000;
        while (cmp(l,r) != 0) {
            long double mid=(l+r)/2;
            if (ok(mid))
                r = mid;
            else l = mid;
        }
        printf("Case #%d: %.8lf\n",o, (double)l);

    }
}
