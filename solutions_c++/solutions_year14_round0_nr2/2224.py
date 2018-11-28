#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    double x, f, c, r, ans;
    int T=0, t;
    scanf("%d", &t);
    while(t--) {
        scanf("%lf%lf%lf", &c, &f, &x);
        r = 2; ans = 0;
        while(x/r > c/r + x/(r+f)) {
            //fprintf(stderr, "%lf\n", c/r);;
            ans += c/r;
            r += f;
        }
        ans += x/r;
        printf("Case #%d: %.7f\n", ++T, ans);
    }
    return 0;
}
