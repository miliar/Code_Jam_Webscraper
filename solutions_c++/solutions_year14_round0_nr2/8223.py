#include <cstdio>
#include <algorithm>
using namespace std;

double C, F, X;
double ans;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("oo.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    while(t--) {
        scanf("%lf%lf%lf", &C, &F, &X);
        ans = 11111111;
        double add = 0, f = 2;
        while(true) {
            if(add + X/f > ans) break;
            ans = min(ans, add + X/f);
            add += C/f;
            f += F;
        }
        printf("Case #%d: %.7f\n", cas++, ans);
    }
    return 0;
}


