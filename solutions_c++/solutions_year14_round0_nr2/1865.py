#include <stdio.h>
double c, f, x;
bool calc(double t){
    double v = 2;
    while (t > -1e-8 && t * v < x - 1e-8){
        t -= c / v;
        v += f;
    }
    return t > -1e-8;
}
int main(){
    int T, ri = 1, k;
    double l, r, z;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%lf%lf%lf", &c, &f, &x);
        l = 0; r = x * 0.5;
        for (k = 0; k < 100; k++){
            z = (l + r) * 0.5;
            if (calc(z)) r = z;
            else l = z;
        }
        printf("Case #%d: %.7f\n", ri++, r);
    }
    return 0;
}
