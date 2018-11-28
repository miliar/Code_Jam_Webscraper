#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main() {
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
    int T;
    int cas = 1;
    double C,F,X;
    scanf("%d",&T);
    while (T--) {
        scanf("%lf %lf %lf",&C, &F, &X);
        double V = F * (X - C) / C;
        double v = 2;
        double ans = 0;
        while (v < V) {
            ans += C / v;
            v += F;
        }
        ans += X / v;
        printf("Case #%d: %.7lf\n",cas++,ans);
    }
    return 0;
}
