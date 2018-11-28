#include <string.h>
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    double cost, earn_more_per_sec, target;
    int num_case;
    scanf("%d", &num_case);

    for (int ncas = 0; ncas < num_case; ++ncas) {
        scanf("%lf %lf %lf", &cost, &earn_more_per_sec, &target);

        double need_time = 0;
        double earn_per_sec = 2;
        
        while (true) {
            double time1 = target / earn_per_sec;
            double time2 = cost / earn_per_sec + target / (earn_per_sec + earn_more_per_sec);
            if (time1 <= time2) {
                need_time += time1;
                break;                
            } else {
                need_time += cost / earn_per_sec;
                earn_per_sec += earn_more_per_sec;
            }
        }
        printf("Case #%d: %.7f\n", ncas+1, need_time);        
    }
    return 0;

}
