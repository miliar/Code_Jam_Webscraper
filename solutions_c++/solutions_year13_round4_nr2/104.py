#include<stdio.h>
int main() {
    int casN;
    scanf("%d", &casN);
    for (int casI = 0; casI < casN; casI++) {
        int n; 
        long long p, sum, run, an1, an2;
        scanf("%d%lld", &n, &p);
        run = 1ll << n-1;
        sum = 0;
        an1 = 0;
        while (sum < p) {
            sum += run;
            run >>= 1;
            an1 ++;
            if (an1 > n) break;
        }
        if (an1 <= n) an1 = (1ll << an1) - 2;
        else an1 = (1ll << n) - 1;
        run = 1ll << n-1;
        sum = 1ll << n;
        an2 = 0;
        while (sum > p) {
            sum -= run;
            run >>= 1;
            an2 ++;
        }
        an2 = (1ll << n) - (1ll << an2);
        printf("Case #%d: %lld %lld\n", casI+1, an1, an2);
    }
    return 0;
}
