#include <cstdio>
#include <cstring>

#define min(a, b) (a < b ? a : b)

using namespace std;

int T, C=1;
double c, f, x;

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%lf %lf %lf",&c,&f,&x);
        double resp = x/2.0;
        double atu = 0.0;
        for (int k=1;k<50000000;k++) {
            atu += c/(2.0+(k-1)*f);
            double tot = atu + x/(2.0+k*f);
            resp = min(resp, tot );
        }

        printf("%.8lf\n",resp);
    }

    return 0;
}
