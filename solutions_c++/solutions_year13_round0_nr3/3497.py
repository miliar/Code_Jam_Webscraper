#include <stdio.h>

int r[1000 * 1000 * 10];

bool checkFor(long long a) {
    int z[20];
    int u = 0;
    while (a > 0) {
        z[u++] = a % 10;
        a /= 10;
    }
    int u1 = 0;
    u--;
    while (u > u1)
        if (z[u--] != z[u1++])
            return false;

    return true;
}

int fin(long long a) {
    long long left = 0;
    long long right = 1000 * 1000 * 10 + 1;
    while (left < right - 1)
        if ((left + right) / 2 * ((left + right) / 2) >= a)
            right = (left + right) / 2;
        else
            left = (left + right) / 2;

    return left;
}

int main() {
    r[0] = 0;
    for (long long i = 1; i <= 1000 * 1000 * 10; i++)
        r[i] = r[i - 1] + (checkFor(i) && checkFor(i * i));

    int t;
    scanf("%d", &t);
    long long a, b;
    for (int i = 1; i <= t; i++) {
        scanf("%lld%lld", &a, &b);
        int x = fin(b);
        if ((x + 1) * (x + 1) == b)
            x++;
        printf("Case #%d: %d\n", i, r[x] - r[fin(a)]);
    }
    return 0;
}
