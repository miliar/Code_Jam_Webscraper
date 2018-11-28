#include <iostream>
#include <cstdio>
#include <cmath>

const double C2 = 2.0;

void calculate() {
    double c, f, x, t = 0.00;
    scanf("%lf%lf%lf", &c, &f, &x);
    int n = floor(x/c - C2/f);
    n = (n < 0) ? 0 : n;

    t = x/(2+n*f);
    for(int i=0; i<n; i++) {
        t+=c/(2+i*f);
    }
    printf("%0.7lf\n", t);
}

int main() {
    int cases, i=0;
    scanf("%d",&cases);
    for(i =1; i<=cases; i++) {
        printf("Case #%d: ", i);
        calculate();
    }
}