#include <stdio.h>
#include <string.h>
#define LL long long

LL get_earliest(LL N){
    if(N==0){
        return -1;
    }
    bool seen[10];
    memset(seen, 0, sizeof(seen));
    int nseen = 0;
    LL i = 0;
    while(nseen < 10){
        ++i;
        LL x = N * i;
        while(x){
            LL d = x % 10;
            if(!seen[d]){
                seen[d] = true;
                ++nseen;
            }
            x /= 10;
        }
    }
    return i;
}

void test_all(void){
    LL M = 0;
    LL m = 0;
    for(LL N=0;N <= 10000000;++N){
        LL sol = get_earliest(N);
        if(sol<m){
            m = sol;
        }
        if(sol>M){
            M = sol;
        }
    }
    printf("Range: %lld, %lld\n", m, M);
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        int N;
        scanf("%d", &N);
        LL sol = get_earliest(N);
        if(sol<0){
            printf("Case #%d: INSOMNIA\n", t);
        }else{
            printf("Case #%d: %lld\n", t, sol*N);
        }
    }
}
