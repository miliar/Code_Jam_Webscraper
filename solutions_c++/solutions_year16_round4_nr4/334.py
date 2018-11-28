#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int a[4];
int f[5][1 << 4];

int main() {
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, res = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                int ch;
                while (ch= getchar(), !isdigit(ch));
                if (ch == '1') res |= 1 << (i * n + j);
            }
        int ans = 1 << 30;
        for (int mask = 0; mask < 1 << (n * n); ++mask) {
            if ((mask & res) != res) continue;
            int flag = 1;
            for (int i = 0; i < n; ++i)
                a[i] = i;

            do {
                memset(f, 0, sizeof(f));
                f[0][0] = 1;
                for (int i = 0; i < n; ++i) {
                    int x = a[i];
                    for (int opt = 0; opt < 1 << n; ++opt)
                        if (f[i][opt]) {
                            int t = mask >> (x * n) & ((1 << n) - 1);
                            if ((opt & t) == t) flag = 0;
                            for (int k = 0; k < n; ++k)
                                if ((t >> k & 1) && !(opt >> k & 1))
                                    f[i + 1][opt | (1 << k)] = 1;
                        }
                }
            } while (next_permutation(a, a + n));
            
            if (flag) ans = min(ans, (int)__builtin_popcount(mask ^ res));
        }
        static int ca = 0;
        printf("Case #%d: %d\n", ++ca, ans);
    }
    return 0;
}
