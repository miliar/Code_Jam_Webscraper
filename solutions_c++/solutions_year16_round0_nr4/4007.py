#include <cstdio>

using namespace std;

typedef unsigned long long ll;

ll power(ll x, ll y) {
    if (y == 0) return 1;
    return x * power(x, y - 1);
}

void solve(int k, int c, int s) {
    ll gap = power(k, c-1);
    ll x = 1;
    for (int i = 0; i < k; i++) {
        printf(" %lld", x);
        x += gap;
    }
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d:", i);
        int K, C, S;
        scanf("%d%d%d", &K, &C, &S);
        solve(K, C, S);
    }
    return 0;
}
