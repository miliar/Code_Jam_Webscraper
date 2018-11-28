#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

long long p[15][17];
int dig[20];

int main(){
        freopen("c.in", "r", stdin);
        freopen("c1.out", "w", stdout);

        int tt, ca = 0;
        scanf("%d", &tt);

        for (int i = 2; i <= 10; i ++){
                p[i][0] = 1;
                for (int j = 1; j < 17; j ++) p[i][j] = p[i][j-1] * i;
        }

        while (tt--) {
                printf("Case #%d:\n", ++ca);
                int n, tot;
                scanf("%d%d", &n, &tot);
                n /= 2;
                int x = (1 << (n-1)) + 1;
                for (int i = 0; i < tot; i ++) {
                        int t = x;
                        for (int j = 0; j < n; j ++, t /= 2) dig[j] = t & 1;

                        for (int j = n - 1; j >= 0; j --) printf("%d", dig[j]);
                        for (int j = n - 1; j >= 0; j --) printf("%d", dig[j]);
                        
                        for (int base = 2; base <= 10; base ++){
                                long long y = 0;
                                for (int j = 0; j < n; j ++) y += dig[j] * p[base][j];
                                printf(" %lld", y);
                        }

                        putchar('\n');
                        x += 2;
                }
        }
}
