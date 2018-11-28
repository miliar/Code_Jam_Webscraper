#include <cstdio>

long long unsigned int gcd(long long val1, long long val2)
{
    long long unsigned int tmp;

    while(val2) { 
        tmp = val2;
        val2 = val1 % val2;
        val1 = tmp;
    }

    return val1;
}

int main()
{
    int caseCount;

    scanf(" %d", &caseCount);
    for(int caseIndex = 1; caseIndex <= caseCount; caseIndex++) {
        long long unsigned int P, Q, tmp;

        scanf(" %lld/%lld", &P, &Q);

        tmp = gcd(P, Q);
        P /= tmp;
        Q /= tmp;

        if((Q & (Q - 1)) == 0) {
            int shift = 0;
            for(int shift = 0;; shift++, P <<= 1) {
                if(P & Q) {
                    printf("Case #%d: %d\n", caseIndex, shift);
                    break;
                }
            }
        }
        else {
            printf("Case #%d: impossible\n", caseIndex);
        }
    }

    return 0;
}
