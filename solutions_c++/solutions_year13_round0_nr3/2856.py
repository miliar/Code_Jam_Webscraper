#include <stdio.h>
#include <math.h>

bool isfair(long long num) {
    if (num%10 == 0) return false;
    long long n = num;
    long long rev = 0;
    while (n > 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return num == rev;
}

int count(long long a, long long b) {
    long long start = ceil(sqrt(a));
    long long end = sqrt(b);
    int count = 0;
    for (long long i = start; i <= end; i++)
        if (isfair(i) && isfair(i*i))
            count++;
    return count;
}

int main(void) {
    int tc;
    long long a, b;
    scanf("%d", &tc);
    for (int i = 0; i < tc; i++) {
        scanf("%lld %lld", &a, &b);
        printf("Case #%d: %d\n", i+1, count(a, b));
    }
    return 0;
}
