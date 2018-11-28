#include <bits/stdc++.h>

bool work(int n) {
    int mask = 0;
    for (int i = 1; i <= 1000000; ++ i) {
        long long x = n * 1ll * i;
        do {
            mask |= 1 << (x % 10);
            x /= 10;
        } while (x);
        if (mask == (1 << 10) - 1) {
            printf("%I64d\n",n * 1ll * i);
            return true;
        }
    }
    return false;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",++ca);
        if (!work(n)) {
            puts("INSOMNIA");
        }
    }
}
