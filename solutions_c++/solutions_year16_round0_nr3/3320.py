#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int N = 16, C = 50;
    int V[40];
    V[N-1] = 1;
    for (int i = 0; i < N-1; i++) {
        V[i] = 0;
    }

    int found = 0;
                printf("Case #1:\n");

    while (found < C) {
        bool ok = true;
        int p = 0; bool carry = true;
        while (carry) {
            if (V[p] == 0) {
                V[p] = 1; carry = false;
            }
            else {
                V[p] = 0;
            }
            p++;
        }
        long long divs[11];
        for (int base = 2; base <= 10; base++) {
            long long val = 0;

            for (int i = N-1; i >= 0; i--) {
                val = base * val + V[i];
            }
            //fprintf(stderr, "b%d: %lld\n", base, val);
            for (long long d = 2; d*d <= val; d++) {
                if (val % d == 0) {
                    divs[base] = d;
                    goto GOOD;
                }
            }
            ok = false;
            GOOD: int a =2;
        }

        if (ok && V[0] == 1) {
            for (int i = N-1; i >= 0; i--) {
                printf("%d", V[i]);
            }
            printf(" ");
            for (int b = 2; b < 10; b++) printf("%lld ", divs[b]);
            printf("%lld\n", divs[10]);
            found++;
        }
    }
    return 0;
}
