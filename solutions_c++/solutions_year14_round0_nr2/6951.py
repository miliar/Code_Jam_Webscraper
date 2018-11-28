#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;


double to7dig(double x) {
    x *= 10e8;
    x = floor(x);
    return x / 10e8;
}

int main()
{
    freopen("cookie.in", "r", stdin);
    freopen("cookie.out", "w", stdout);
    int v;
    scanf("%d", &v);
    for(int u = 1; u <= v; u++) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double dt = c / f;
        if(c >= x) printf("Case #%d: %lf\n", u, x / 2);
        else {
            double t = c / 2;
            double k = 2;
            double num_coins = c;
            while(num_coins < x) {
                double delta = (x - num_coins) / k;
                if(delta >= dt) {
                    k += f;
                    num_coins = c;
                    t += c / k;
                } else {
                    t += delta;
                    num_coins = x;
                }
            }
            printf("Case #%d: %lf\n", u, t);
        }
    }
    return 0;
}
