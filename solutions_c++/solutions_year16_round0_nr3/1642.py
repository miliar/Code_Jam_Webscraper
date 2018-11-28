#include <stdio.h>
#include <string.h>
#define LL long long

int main(){
    int T, N, J;
    LL divisors[11];
    scanf("%d\n%d %d", &T, &N, &J);
    printf("Case #1:\n");
    for(int x=1; x<=J; ++x){
        memset(divisors, 0, sizeof(divisors));
        int xx = 1 + 2 * x;
        int d = 0;
        while(xx){
            int b = xx%2;
           
            for(int i=2;i<=10;++i){
                divisors[i] = divisors[i]*i+b;
            }
            
            printf("%d", b);
            xx /= 2;
            d += 1;
        }
        
        int z = N-2*d;
        for(int i=0;i < z; ++i){
            printf("0");
        }
        
        xx = 1 + 2 * x;
        while(xx){
            printf("%d", xx%2);
            xx /= 2;
        }

        for(int b=2;b<=10;++b){
            printf(" %lld",divisors[b]);
        }
        printf("\n");
    }
    return 0;
}
