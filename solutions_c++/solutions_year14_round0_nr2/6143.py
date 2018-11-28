#include <cstdio>
using namespace std;

int calcN(double C, double F, double X) {
    int n = X/C - 2/F;
    if (n <= 0) {
        return 0;
    }
    return n;
}

double totalTime(double C, double F, double X, int n) {
    double res = 0;
    int i;
    for (i = 0; i < n; ++i) {
        res += C / (2 + F*i);
    }
    res += X / (2 + F*n);
    return res;
}

int main() {
    freopen("B.txt", "r", stdin);
    int T, ca;
    scanf("%d", &T);
    for (ca = 1; ca <= T; ++ca) {
        printf("Case #%d: ", ca);
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        int n = calcN(C, F, X);
        printf("%.7lf\n", totalTime(C, F, X, n));
    }
    return 0;
}