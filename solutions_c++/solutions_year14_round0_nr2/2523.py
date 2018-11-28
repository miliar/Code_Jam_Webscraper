#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

double best_time(double c, double f, double x)
{
    double time = 0.0;
    double cookies = 0.0;
    double rate = 2.0;

    while(cookies < x) {
        if((x)/rate > (c/rate + x/(rate+f))) {
            time += c/rate;
            rate += f;
        } else {
            time += (x/rate);
            return time;
        }
    }

    return time;
}

int main()
{
    int t;
    double c, f, x;
    double ans = 0.0;

    freopen("B-large.in.txt","r",stdin);
    freopen("outpooo.txt","w",stdout);
    scanf("%d", &t);
    for(int i = 1;i <= t;i++) {
        scanf("%lf %lf %lf",&c, &f, &x);
        ans = best_time(c, f, x);
        printf("Case #%d: %.7lf\n",i, ans);
    }
    return 0;
}


