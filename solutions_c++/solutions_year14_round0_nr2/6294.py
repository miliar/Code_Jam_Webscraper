#include <stdio.h>

void solve_problem() {
    double C, F, X;
    scanf("%lf %lf %lf", &C, &F, &X);
    double num_seconds = 0;
    int current_factories = 0;
    while (1) {
        double rate = 2 + F * current_factories;
        double time_remaining = (double)X / (double)rate;
        // or if we buy a new factory...
        double factory_time = (double)C / (double)rate;
        current_factories++;
        rate = 2 + F * current_factories;
        double new_time = (double)X / (double)rate + factory_time;
        if (new_time <= time_remaining) {
            // I guess we have to buy the factory...
            num_seconds += factory_time;
            continue;
        }
        // No factory for us!
        num_seconds += time_remaining;
        break;
    }
    printf("%.28f", num_seconds);
}

int main(int argc, char **argv) {
    int T;
    scanf("%i", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%i: ", i);
        solve_problem();
        printf("\n");
    }
    return 0;
}
