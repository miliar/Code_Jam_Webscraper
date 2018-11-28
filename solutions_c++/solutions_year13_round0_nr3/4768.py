#include <cstdio>
#include <cmath>
#include <cstring>

long long a, b;

bool isfands(long long n) {
    char tmps[100];
    sprintf(tmps, "%lld", n);
    int len;
    len = strlen(tmps);
    for (int i = 0; i < len / 2; i++) {
        if (tmps[i] != tmps[len - i - 1]) return false;
    }
    long long rt = sqrt(n);
    if (rt * rt != n) return false;
    sprintf(tmps, "%lld", rt);
    len = strlen(tmps);
    for (int i = 0; i < len / 2; i++) {
        if (tmps[i] != tmps[len - i - 1]) return false;
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf ("%lld%lld", &a, &b);
        long long count = 0;
        for (long long i = a; i <= b; i++) {
            if (isfands(i)) count++;
        }
        printf("Case #%d: %lld\n", tc, count);
    }    
    return 0;
}
