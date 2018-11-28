#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << "\n"
#define MOD ((int)(1e9+7))
#define EPS 1e-6
int T;
double C, F, X;


double minTime() {
    double minS = (X / 2.0);
    double acum = (C / 2.0);
    double tmp = 0.0, total = 0.0;
    double rate = 2.0 + F;
    if (X < C) {
        return minS;
    }
    else {
        while (true) {
            tmp = acum + X/rate;
            if (tmp < minS) {
                minS = tmp;
                acum += C/rate;
                rate += F;
            }
            else break;
        }
    }
    return minS;
}
int main() {
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        scanf ("%lf %lf %lf", &C, &F, &X);
        double ans = minTime();
        printf("Case #%d: %.7f\n", i, ans);
    }
}