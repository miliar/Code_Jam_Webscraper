#include <cstdio>
#define MAX_FARMS 100100

int n_cases;
double farm_cost, farm_bonus, goal;

double time(int n_farms);

int main() {
    scanf("%d", &n_cases);
    for (int t = 1; t <= n_cases; t++) {
        scanf("%lf %lf %lf", &farm_cost, &farm_bonus, &goal);

        int start = 1;
        int end = MAX_FARMS;
        double best = time(0);
        while (start <= end) {
            int mid = (start+end)/2;
            double cur_time = time(mid);
            double prev_cur_time = time(mid-1);
            if (cur_time < best) {
                best = cur_time;
            }
            if (prev_cur_time > cur_time) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        printf("Case #%d: %.7lf\n", t, best);
    }
        
    return 0;
}

double time(int n_farms) {
    double result = goal / (2 + n_farms * farm_bonus);
    for (int i = 0; i < n_farms; i++) {
        result += farm_cost/(2 + farm_bonus * i);
    }
    return result;
}
