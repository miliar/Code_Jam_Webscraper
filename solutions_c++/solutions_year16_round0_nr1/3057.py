#include <stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        long long N;
        int markcnt=0;
        int mark[10] = {0,0,0,0,0,0,0,0,0,0};
        scanf("%lld", &N);
        if(N == 0){ printf("Case #%d: INSOMNIA\n", i+1); continue; }
        long long dup = N;
        while(markcnt < 10){
            long long temp = dup;
            while(temp > 0){
                if(!mark[temp%10]) mark[temp%10] = 1, markcnt++;
                temp /= 10;
            }
            dup += N;
        }
        printf("Case #%d: %lld\n", i+1, dup-N);
    }
}