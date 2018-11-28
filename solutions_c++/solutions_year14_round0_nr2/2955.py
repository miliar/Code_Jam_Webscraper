#include <cstdio>
#include <algorithm>

using namespace std;

double C, F;

double numSeconds(double r, double X);

int main(int argc, char * argv[]) {
    double X;
    int T, c = 1;

    scanf("%d", &T);
    while (T--) {
        scanf("%lf %lf %lf", &C, &F, &X);
        printf("Case #%d: %.7lf\n", c++, numSeconds(2.0, X));
    }
    return 0;
}

double numSeconds(double r, double X) {
    if ((C / r + X / (r + F) < X / r)) return C / r + numSeconds(r + F, X);
    else return X / r;
}