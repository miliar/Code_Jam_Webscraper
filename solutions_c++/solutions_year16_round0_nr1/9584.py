#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

int cnt[15];
int mc;

void foo(ull x){
    if(!x) {cnt[0]++; if(cnt[0] == 1) mc++; return;}
    while(x){
        cnt[x%10]++;
        if(cnt[x%10] == 1) mc++;
        x/=10;
    }
}

int main(int argc, char const *argv[]){
    int tt;
    ull N;
    scanf("%d", &tt);
    for(int T = 1; T <= tt; T++){
        ull l1, l2;
        scanf("%llu", &N);
        mc =0 ;
        memset(cnt, 0, sizeof cnt);
        for(int i = 1; i <= 100000000 && mc < 10; i++){
            if(N != (i*N)/i){
                printf("FUDEEEEEEEEEEEEEEEEEEU! %llu\n", N);
                return 0;
            }
            foo(i*N);
            if(mc >= 10) N = i*N;
            
        }
        if(mc == 10) printf("Case #%d: %llu\n", T, N);
        else  printf("Case #%d: INSOMNIA\n", T);

    }



    return 0;
}