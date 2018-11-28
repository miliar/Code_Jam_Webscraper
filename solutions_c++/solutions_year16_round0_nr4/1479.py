#include <bits/stdc++.h>

using namespace std;
// const int MaxN = ;
// const int MOD = ;

int main() {
    freopen("D-small-attempt0.in", "rt", stdin);
    freopen("D-small.out", "wt", stdout);
    int t;
    scanf("%d", &t);
    for (int cs = 0; cs < t; ++cs) {
        printf("Case #%d: ", cs + 1);
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        for (int i = 0; i < k; ++i) {
            printf("%d ", i + 1);
        }
        printf("\n");
    }
    return 0;
}
