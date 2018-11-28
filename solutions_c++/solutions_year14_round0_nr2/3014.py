#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        double cost, rate, win;
        scanf("%lf %lf %lf", &cost, &rate, &win);
        double tim = 0;
        double grow = 2;
        double ans = win / 2.0;
        for (int buy = 1; buy <= 1000001; buy++) {
            tim += cost / grow;
            grow += rate;
            ans = min(ans, tim + (win / grow));
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
