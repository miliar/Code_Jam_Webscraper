#include <bits/stdc++.h>

using namespace std;
// const int MaxN = ;
// const int MOD = ;

int main() {
        ios_base::sync_with_stdio(0);
        freopen("D-small-attempt0.in", "rb", stdin);
        freopen("D-small.out", "wb", stdout);
        int t;
        scanf("%d", &t);
        for (int cs = 0; cs < t; ++cs) {
                printf("Case #%d: ", cs + 1);
                int x, r, c;
                scanf("%d%d%d", &x, &r, &c);
                if (x >= 7) {
                        printf("RICHARD\n");
                        continue;
                }
                if ((r * c) % x == 0) {
                        if (x == 1 || x == 2) {
                                printf("GABRIEL\n");
                                continue;
                        } else if (x == 3 && min(r, c) >= 2) {
                                printf("GABRIEL\n");
                                continue;
                        } else if (x == 4 && min(r, c) >= 3) {
                                printf("GABRIEL\n");
                                continue;
                        } else if (x == 5 && min(r, c) >= 3) {
                                printf("GABRIEL\n");
                                continue;
                        } else if (x == 6 && min(r, c) >= 4) {
                                printf("GABRIEL\n");
                                continue;
                        }
                }
                printf("RICHARD\n");
        }
        return 0;
}
