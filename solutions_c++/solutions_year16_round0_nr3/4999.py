#include <bits/stdc++.h>

void work(int n,int m) {
    for (int mask = 0; mask < 1 << n && m > 0; ++ mask) {
        if ((~mask & 1) || (~mask >> n - 1 & 1)) continue;
        std::vector<long long> vec;
        for (int base = 2; base <= 10; ++ base) {
            long long val = 0;
            for (int i = 0; i < n; ++ i) {
                val = val * base + (mask >> i & 1);
            }
            for (long long i = 2; i * i <= val; ++ i) {
                if (val % i == 0) {
                    vec.push_back(i);
                    break;
                }
            }
        }
        if (vec.size() != 9) continue;
        m --;
        for (int i = 0; i < n; ++ i) {
            printf("%d",mask >> i & 1);
        }
        for (int i = 0; i < 9; ++ i) {
            printf(" %I64d",vec[i]);
        }
        puts("");
    }
}

int main() {
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        int n,m;
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",++ca);
        work(n,m);
    }
}
