#include <cstdio>

bool visited[10];

bool ok() {
    for (int i = 0; i < 10; ++i)
        if (visited[i] == false)
            return false;
    return true;
}

void go(long long k) {
    while (k) {
        long long tmp = k % 10LL;
        visited[tmp] = true;
        k /= 10LL;
    }
}

long long solve(long long n) {
    if (n == 0) return -1;
    for (int i = 0; i < 10; ++i)
        visited[i] = false;

    long long tmp;
    tmp = n;
    go(tmp);

    while (ok() == false) {
        tmp += (long long)n;
        go(tmp);
    }
    
    return tmp;
}

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 1; i <= n; ++ i) {
        long long k;
        scanf("%lld", &k);
        long long res = solve(k);
        printf("Case #%d: ", i);
        if (res == -1) puts("INSOMNIA");
        else printf("%lld\n", res);
    }

    return 0;
}
