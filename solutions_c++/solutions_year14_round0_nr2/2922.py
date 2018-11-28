#include <iostream>

using namespace std;

double solve(double C, double F, double X)
{
    double cps = 2.0; // cookie per second
    double min_time = X / cps;
    double next_time = C / cps;

    while (1) {
        double n_t = next_time + (X / (cps + F));
        if (n_t < min_time) min_time = n_t;
        else return min_time;

        cps += F;
        next_time += C / cps;
    }
}


int main(void) {
    int c;
    double C, F, X;
    cin >> c;

    for (int i = 0; i < c; i++) {
        cin >> C >> F >> X;
        printf("Case #%d: %.8f\n", i + 1, solve(C, F, X));
    }
}