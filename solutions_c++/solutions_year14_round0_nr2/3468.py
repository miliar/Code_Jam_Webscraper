#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T; scanf("%d", &T);
    int cas = 0;
    while(T--) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        double cur = 0;
        double get = 2.0;
        double ans = X / 2.0;
        while(cur < ans) {
            ans = min(ans, cur + X / get);
            cur += C / get;
            get += F;
        }
        printf("Case #%d: %.10f\n", ++ cas, ans);
    }

    return 0;
}
