#include <cstdio>

int main() {
    int foi;
    long long unsigned od, nn, d, n, i;
    scanf("%llu", &n);
    for(i=1;i<=n;i++) {
        scanf("%llu", &nn);
        if(nn==0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;        
        }
        foi=0;
        od = nn;
        while(foi != (1<<10)-1){
            d=od;
            while(d>=10) {
                foi |= 1 << d%10;
                d/=10;
            }            
            foi |= 1 << d;
            od+=nn;
        }
        printf("Case #%d: %llu\n", i, od-nn);
    }
    
    return 0;
}