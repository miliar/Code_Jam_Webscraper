#include <bits/stdc++.h>

const double eps = 1e-3;

int dcmp(double x) {
    return x < -eps ? -1 : x > eps;
}

int n;
double V,X;
double R[100],C[100];

double work() {
    // solve small dataset

    if (n == 1) {
        double t = V / R[0];
        if (dcmp(V * X - (t * R[0] * C[0])) != 0) {
            return false;
        }
        printf("%.10f\n",t);
        return true;
    }

    double tmp = R[1] * C[1]  - R[1] * C[0];
    if (dcmp(tmp) == 0) {
        return false;
    }

    double t[2];
    t[1] = (V * X - V * C[0]) / tmp;

    if (dcmp(t[1]) < 0) {
        return false;
    }

    t[0] = (V - R[1] * t[1]) / R[0];
    
    if (dcmp(t[0]) < 0) {
        return false;
    }

    printf("%.10f\n",std::max(t[1],t[0]));
    return true;
}

int main(int argc,char **args) {
    if (argc > 1) {
        freopen(args[1],"r",stdin);
        freopen("data.txt","w",stdout);
    }
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        scanf("%d%lf%lf",&n,&V,&X);
        for (int i = 0; i < n; ++ i) {
            scanf("%lf%lf",R + i,C + i);
        }
        printf("Case #%d: ",++ca);
        if (!work()) {
            puts("IMPOSSIBLE");
        }
    }
}
