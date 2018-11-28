#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cstdio>
using namespace std;

const int LIMIT = 300010;
double solve(double C, double F, double X) {
    double cps = 2;
    double ans = 1e60;
    double sum = 0;
    //for (int i = 0; i < LIMIT; i++) {
    while (sum < ans) {
        ans = min(ans, sum + X / cps);
        //if (sum > ans + 1e-8) break;
        sum += C / cps;
        cps += F;
    }
    return ans;
}

int main() {
    freopen("p2l.in", "r", stdin);
    freopen("p2l.out", "w", stdout);
    int T, Case = 1;
    scanf("%d", &T);
    while (T--) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("Case #%d: %.10f\n", Case++, solve(C, F, X));
    }
    return 0;
}

