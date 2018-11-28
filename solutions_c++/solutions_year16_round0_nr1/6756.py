#include <stdio.h>
#include <stdlib.h>

int main()
{

    long flag;
    int T, t, b;
    long N, n;
    scanf("%d", &T);
    for(t = 1; t <= T; t++) {
        scanf("%ld", &N);
        if(N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
        } else {
            flag = 1023;
            long p = 1;
            while(flag) {
                n = p * N;
                while(n>0) {
                    b = n%10;
                    flag &= ~(1 << b); // clearing b-th bit
                    n/=10;
                }
                p += 1;
            }
            printf("Case #%d: %ld\n", t, (p-1)*N);
        }
    }
    return 0;
}
