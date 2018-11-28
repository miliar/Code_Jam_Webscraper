#include <cstdio>

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, i, n;
    double c, f, x;
    scanf("%d", &t);
    for (i = 1; i <= t; i++){
        scanf("%lf %lf %lf", &c, &f, &x);
        double ctime = x/2, ptime = x, ftime = 0;
        for (double speed = 2.0; ctime < ptime; ){
            ptime = ctime;
            ftime = ftime + c/speed;
            speed += f;
            ctime = ftime + x/speed;
        }
        printf("Case #%d: %.7lf\n", i, ptime);
    }
}
