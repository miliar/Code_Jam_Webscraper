#include <stdio.h>
#include <math.h>

int lcd(int p, int q); // largest common divisor
int two_exp(int n);

int main()
{
    const int kMaxGen = 40;
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; ++t) {
        int p, q;
        scanf("%d/%d", &p, &q);
        // factor
        int d = lcd(p, q);
        p /= d;
        q /= d;
        int e = two_exp(q);
        int gen = -1;
        if (e > 0 && e <= kMaxGen) {
            gen = e - (int)log2(p);
        }
        printf("Case #%d: ", t);
        if (gen > 0) {
            printf("%d", gen);
        } else {
            printf("impossible");
        }
        printf("\n");
    }
}

int lcd(int p, int q)
{
    if (p < 0 || q < 0) return -1;  // error
    if (p > q) {
        int t = q;
        q = p;
        p = t;
    }
    while (int r = (q % p)) {
        q = p;
        p = r;
    }
    return p;
}

int two_exp(int n)
{
    int e = 0;
    while (n >= 2) {
        if (n % 2) return -1;
        n /= 2;
        e++;
    }
    return e;
}
