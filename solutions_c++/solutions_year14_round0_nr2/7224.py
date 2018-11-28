#include <stdio.h>

using namespace std;

int main() {
    freopen ("fin.in", "r", stdin);
    freopen ("fout.out", "w", stdout);
    double farm_price, farm_rate, final_sum, act_rate, act_time = 0, time_pos, time_farm, prev_time;
    int T, count;
    scanf ("%d", &T);
    for (count = 1; count <= T; ++count) {
        scanf ("%lf %lf %lf", &farm_price, &farm_rate, &final_sum);
        act_rate = 2;
        prev_time = final_sum/act_rate;
        act_time = 0;
        do {
            time_farm = act_time + farm_price/act_rate + final_sum/(act_rate + farm_rate);
            if (time_farm > prev_time) {
                printf ("Case #%d: %.7lf\n", count, prev_time);
                break;
            }
            prev_time = time_farm, act_time += farm_price/act_rate, act_rate += farm_rate;
        } while (true);
    }
    return 0;
}
