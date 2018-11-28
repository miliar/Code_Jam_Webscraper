#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAX = 10000000;

long long reverse_int(long long n) {
    long long result = 0;
    while (n) {
        result = result * 10 + n % 10;
        n /= 10;
    }
    return result;
}

long long is_palindrome(long long n) {
    return reverse_int(n) == n;
}

int ok[MAX + 10], sum[MAX + 10];
long long sqr[MAX + 10];

int main() {
    for (long long i = 1; i <= MAX; ++i) {
        sqr[i] = i * i;
        if (is_palindrome(i) && is_palindrome(i * i)) {
            ok[i] = 1;
        }
    }
    sum[0] = 0;
    for (int i = 1; i <= MAX; ++i) {
        sum[i] = sum[i - 1] + ok[i];
    }
    int tott;
    scanf("%d", &tott);
    for (int curt = 0; curt < tott; ++curt) {
        long long a, b;
        scanf("%lld%lld", &a, &b);
        int l = lower_bound(sqr, sqr + MAX + 1, a) - sqr;
        int r = upper_bound(sqr, sqr + MAX + 1, b) - sqr;
        printf("Case #%d: %d\n", curt + 1, sum[r - 1] - sum[l - 1]);
    }
    return 0;
}
