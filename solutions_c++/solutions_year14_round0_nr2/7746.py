#include <iostream>
#include <cstdio>

using namespace std;
main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    double C, F, X, d=(double)2.0, k;
    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> C >> F >> X;
        double m = 0.0;
        d = 2;
        double ans = X/d;
        while(1) {
            k = m + C/d;
            if(k>ans) break;
            m = k;
            k += (X-C)/d;
            ans = min(ans, k);
            d += F;
        }
        printf("Case #%d: %.7lf\n",t,ans);
    }
}
