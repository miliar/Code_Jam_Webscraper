#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        int farms;
        double ret = 0.0;
        if (X*F-2*C <= F*C) farms = 0;
        else farms = floor((X*F-2*C)/(F*C));
        double speed = 2.0;
        //printf("%d\n", farms);
        for (int i = 0; i <= farms; ++i, speed += F) {
            ret += (i==farms?X:C) / speed;
        }
        printf("Case #%d: %.7f\n", cas, ret);
    }
    return 0;
}
