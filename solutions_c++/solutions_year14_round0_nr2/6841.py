#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

const double eps = 1e-7;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, cnt;
    double C, F, X, now, ans, tmp, cur;

    scanf("%d", &T);
    for (int tcase=1; tcase<=T; tcase++){
        scanf("%lf%lf%lf", &C, &F, &X);

        cur = 2.0;
        now = 0.0;
        ans = X/2.0;
        while (1) {
            now = now + C/cur;
            if (ans<now+eps) break;
            cur += F;
            tmp = now+ X/cur;
            ans = min(ans, tmp);
        }
        printf("Case #%d: %.7lf\n", tcase, ans);
    }

    return 0;
}
