#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("inl.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,o = 0;
    scanf("%d", &t);
    double a,b,c,r,ans;
    while (t--) {
        r = 2;
        scanf("%lf%lf%lf", &a, &b, &c);
        ans = 0;
        while (1) {
            if ((a/r)+(c/(r+b)) >= (c/r)) {
                ans += c/r;
                break;
            }
            else {
                ans += a/r;
                r += b;
            }
        }
        o++;
        printf("Case #%d: %.7lf\n", o, ans);
    }
    return 0;
}
