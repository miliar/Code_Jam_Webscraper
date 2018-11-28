#include <cstdio>

int main() {
    int cases;
    scanf("%d", &cases);
    for (int i = 0; i < cases; ++i) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double rate = 2.0;
        double best_time = 1e9;
        double past_time = 0;
        while (true) {
            if (c / rate + x / (rate + f) < x / rate) {
                past_time += c / rate;
                rate += f;
            } else {
                printf("Case #%d: %f\n", i + 1, past_time + x / rate);
                break;
            }
        }
    }
    return 0;
}
