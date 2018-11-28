#include <iostream>
#include <map>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
int n ;
double R[2], VV[2];
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--) {
        double V, X;
        scanf("%d%lf%lf", &n, &V, &X);
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf", &R[i], &VV[i]);
        }
        double ans = 0;
        bool imp = 0;
        if(n == 1){
            if (VV[0] != X) {
                imp = 1;
            } else {
                ans = V / R[0];
            }
        } else {
            double mi, mx;
            mi = min(VV[0], VV[1]);
            mx = max(VV[0], VV[1]);
            if(mx < X ||  mi > X) {
                imp = 1;
            } else {
                if (VV[0] == VV[1]) {
                    ans = V / (R[0] + R[1]);
                } else {
                    double tmp = V - (X * V - V * VV[0]) / (VV[1] - VV[0]) ;
                    ans = tmp / R[0];
                    if((X * V - V * VV[0]) / (VV[1] - VV[0]) / R[1] > ans) {
                        ans = (X * V - V * VV[0]) / (VV[1] - VV[0]) / R[1];
                    }
                }
            }
        }

        printf("Case #%d: " , ++cas) ;
        if(imp) {
            puts("IMPOSSIBLE");
        } else {
            printf("%.10f\n" , ans) ;
        }

    }
    return 0;
}
