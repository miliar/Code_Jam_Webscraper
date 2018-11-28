#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string.h>

using namespace std;

unsigned long long reverse(unsigned long long n) {
    unsigned long long reversed = 0;
    while (n > 0) {
        reversed = 10 * reversed + n % 10;
        n /= 10;
    }
    return reversed;
}

unsigned long long next(unsigned long long n, unsigned long long target) {
    unsigned long long reversed = reverse(n);
    if (reversed <= target && reversed > n && (reverse(n + 1) > target || reverse(n + 1) <= reversed))
        return reversed;
    return n + 1;
}

int main() {
    int T;
    scanf("%d", &T);
    register int i, cases;
    for (cases = 0; cases < T; cases++) {
        unsigned long long N;
        scanf("%llu", &N);
        
        unsigned long long moves = 0;
        unsigned long long curr = 0;
        while (curr != N) {
            curr = next(curr, N);
            moves++;
        }

        printf("Case #%d: %llu\n", cases + 1, moves);
    }
}
