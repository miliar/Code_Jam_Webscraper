#include <cstdio>
using namespace std;

int counter = 0;
void make() {
    long double speed = 2.0;
    long double best;

    long double c; // cost to buy cookie farm
    long double f; // speed boost gained on buying a cookie farm.
    long double x; // final cookie target

#if 0
    c = 30.5;
    f = 3.14159;
    x = 1999.19990;
    c = 500;
    f = 4;
    x = 2000;
    c = 30;
    f = 1;
    x = 2;
#endif

    scanf("%Lf %Lf %Lf", &c, &f, &x);

    // long double time_without_extra_cookie_farms = 0.0;
    // long double time_with_extra_cookie_farms = 0.0;
    long double time_without = 0.0;
    long double time_with = 0.0;
    long double cookie_farm_time = 0.0;

    do {
        time_with    = (c/speed) + x/(speed+f);
        time_without = x/speed;

        if (time_without <= time_with) {
            best = time_without;
            // printf("breaking out\n");
            break;
        } else {
            /* add cookie buying cost */
            cookie_farm_time += c/speed;
            speed += f;
        }
    } while (1);

    printf("Case #%d: ", ++counter);
    printf("%Lf\n", cookie_farm_time+best);
    return;
}

int main() {
    int t;
    scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
