#include <stdio.h>

int cal(unsigned long long now){
    int st = 0;
    while(now){
            int t = now%10;
            now/=10;
            st|=(1<<t);
    }
    return st;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("outA.out", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int ca=1; ca<=t; ca++){
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", ca);
        if(!n){
            puts("INSOMNIA");
        }else{
            unsigned long long  now = n;
            int st = cal(now);
            while(st != 1023){
                now += n;
                st |= cal(now);
            }
            printf("%llu\n", now);
        }
    }
    return 0;
}
