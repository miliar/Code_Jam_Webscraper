
#include <stdio.h>

double buy(int n, double c, double f, double base_rate) {
    double cost = 0;
    for (int i=1; i<=n; ++i) {
        cost += c/(base_rate + (i-1)*f);
    }
    return cost;
}

double with(int i, double c, double f, double x, double base_rate) {
    // time to buy i + x at base_rate + i*f
    if (i == 0) return x/base_rate;
    return buy(i, c, f, base_rate) + x/(base_rate + i*f);
}

double cost(double c, double f, double x, double base_rate) {
    int i=0;
    double curr = with(i, c, f, x, base_rate);
    double next;
    while (true) {
        next = with(i+1, c, f, x, base_rate);
        if (curr <= next) return curr;
        curr = next;
        i += 1;
    }
}

int main(int argc, char * argv[]) {
    int cases;
    scanf("%d", &cases);
    for (int i=0; i<cases; ++i) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double t = cost(c, f, x, 2);
        printf("Case #%d: %0.7lf\n", i+1, t);
    }
}
