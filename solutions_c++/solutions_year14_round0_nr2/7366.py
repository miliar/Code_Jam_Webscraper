#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

int cmp_asc(const void* p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}

int cmp_desc(const void* p1, const void *p2) {
    return *(int*)p2 - *(int*)p1;
}

int main() {
    int cnt_case = 0;
    scanf("%d", &cnt_case);
    int case_idx = 0;
    while (cnt_case--) {
        ++case_idx;

        // compute here
        double cost = 0.0;
        double farm = 0.0;
        double target = 0.0;
        scanf("%lf %lf %lf", &cost, &farm, &target);

        double rate = 2.0;
        double time = 0.0;
        while (true) {
            if (target / rate > (target / (rate + farm) + (cost / rate))) {
                time += (cost / rate);
                rate += farm;
            } else {
                time += (target / rate);
                break;
            }
        }
        printf("Case #%d: ", case_idx);
        
        // output here
        printf("%.6lf\n", time);
    }
    return 0;
}
