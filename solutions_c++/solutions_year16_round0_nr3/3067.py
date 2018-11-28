#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

unsigned long long get_val(unsigned long long ctr, int base, int n) {
    unsigned long long val, pow, first;
    val = 1;
    pow = base;
    while (ctr>0) {
        if (ctr&1)
            val += pow;
        pow *= base;
        ctr = ctr>>1;
    }
    pow = base;
    first = 1;
    while (n>0) {
        if (n&1)
            first *= pow;
        pow *= pow;
        n = n>>1;
    }
    val += first;
    return val;
}

int get_factor(unsigned long long n) {
    int root = sqrt(n)+1;
    for (int i=2; i<=root; i++) {
        if (n%i == 0)
            return i;
    }
    return -1;
}

int main(void) {
    unsigned long long num, ctr;
    int N, T, J, flag;
    int factor[9], f;
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        scanf ("%d%d", &N, &J);
        printf ("Case #%d:\n", i);
        for(ctr=0; ctr < 1LLU<<(N-2) && J>0; ctr++) {
            flag=0;
            for (int j=2; j<=10; j++) {
                num = get_val(ctr, j, N-1);
                f = get_factor(num);
                if (f==-1) {
                    flag=1;
                    break;
                }
                factor[j-2] = f;
            }
            if (flag==0) {
                printf ("%llu", num);
                for (int j=2; j<=10; j++)
                    printf(" %d", factor[j-2]);
                printf("\n");
                J--;
            }
        }
    }
    return 0;
}
