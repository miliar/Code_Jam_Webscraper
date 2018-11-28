#include <iostream>
#include <cstdio>

using namespace std;

const double RATE = 2, INF = 1000005;

int main()
{
    freopen("in22.txt", "r", stdin);
    freopen("out22.txt", "w", stdout);

    int cn, ci;

    scanf("%d", &cn);
    for(ci = 1; ci <= cn; ci++) {
        int i;
        double r = 0, cr = RATE, ans = INF, t = 0, c, f, x;

        scanf("%lf %lf %lf", &c, &f, &x);

        for(i = 0;i <= x; i++) {
            ans = min(ans, max(0.0, (x - r) / cr) + t);

            if(r < c) {
                double nt = (c - r) / cr;
                r +=  nt * cr;
                t += nt;
            }

            r -= c;
            cr += f;
        }

        printf("Case #%d: %lf\n", ci, ans);
    }
    return 0;
}
