#include <cstdio>
#include <algorithm>
#include <cmath>

double solve() {
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double k = std::max(ceil(x/c - 2/f - 1), 0.0);
    double zaplzafarmy = 0;
    for(int i = 0; i < k; i ++)
        zaplzafarmy += c / (2 + i*f);
    double jeszczesek = x / (2 + k*f);
    return zaplzafarmy + jeszczesek;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++) {
        printf("Case #%d: %.7lf\n", i, solve());
    }
}