#include<iostream>
#include<cstdio>
#include<cstring>


using namespace std;



int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ++ti) {
        printf("Case #%d: ", ti);

        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);

        double t = 0;
        double rate = 2.0;
        while (x > c && x / (f + rate) < ((x - c )/ rate) ) {
            t += (c / rate);
            rate += f;

        }
        printf("%.7lf\n", t + x / rate);
    }

    return 0;

}
