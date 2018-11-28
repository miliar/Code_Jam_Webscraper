#include <cstdio>

int main(){
    long long Case;
    scanf("%lld",&Case);
    for(long long c = 1; c <= Case; ++c){
        long long N;
        scanf("%lld", &N);
        if(N == 0){
            printf("Case #%lld: INSOMNIA\n", c);
        }else{
            unsigned long long test = 0b1111111111;
            long long CN = N;
            while(1){
                long long tmp = CN;
                while(tmp){
                    test &= ~(0x01 << tmp % 10);
                    tmp /= 10;
                }
                if(!test) break;
                else CN += N;
            }
            printf("Case #%lld: %lld\n", c, CN);

        }
    }
}
