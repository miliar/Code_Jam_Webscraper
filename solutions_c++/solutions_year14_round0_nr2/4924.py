#include <cstdio>
#include <cmath>

using namespace std;

const double eps = 1e-6;

int dcmp(double x) {
    if(fabs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, kase = 0;
    double C, F, X;
    scanf("%d", &T);
    while(T--) {
        scanf("%lf%lf%lf", &C, &F, &X);
        double cur_v = 2, cur_sum = 0, ret = 0;
        while(cur_sum < X) {
            double t2x = X / cur_v;
            double t2cx = C / cur_v + X / (cur_v + F);
            if(t2cx < t2x) {
                ret += C / cur_v;
                cur_v += F;
            }
            else  {
                ret += X / cur_v;
                printf("Case #%d: %.7f\n", ++kase, ret);
                break;
            }
        }
    }
    return 0;
}

/*

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

*/
