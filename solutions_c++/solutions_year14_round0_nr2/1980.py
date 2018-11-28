#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int T;
double C, F, X;
int main(int argc, const char * argv[])
{
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        double x1 = 0;
        double s1 = 2.0;
        double s2 = s1 + F;
        double x2 = x1 + C/s1;
        while (true) {
            double y = s2*C/F;
            if (y <= X) {
                x1 = x2;
                s1 = s2;
                s2 = s1 + F;
                x2 = x1 + C/s1;
            } else break;
        }
        double ans = x1 + X/s1;
        printf("Case #%d: %lf\n", t+1, ans);

    }
    return 0;
}

