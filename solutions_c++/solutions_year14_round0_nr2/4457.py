#include <cstdio>

int main()
{
    // freopen("in", "r", stdin);
    // freopen("out", "w", stdout);
    int t, k = 1;
    double c, f, x;
    scanf("%d", &t);
    while(t--) {
        scanf("%lf%lf%lf", &c, &f, &x);
        double rt = x, irs = 2, cot = 0;
        while(1) {
            if((c / irs) + rt / (irs + f) < rt / irs) {
                cot += c / irs;
                irs += f;
            }
            else {
                cot += rt / irs;
                break;
            }
        }
        printf("Case #%d: %.7lf\n", k++, cot);
    }
    return 0;
}
