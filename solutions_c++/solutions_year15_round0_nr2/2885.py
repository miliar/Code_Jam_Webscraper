#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T, D;
int P[10000];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int Case = 1; Case <= T; ++Case) {
        scanf("%d", &D);
        for (int i = 0; i < D; ++i)
            scanf("%d", &P[i]);
        int ans = 1000;
        for (int t = 1; t <= 1000; ++t) {
            int special_t = 0;
            for (int i = 0; i < D; ++i)
                special_t += (P[i] - 1) / t;
            if (special_t + t < ans)
                ans = special_t + t;
        }
        printf("Case #%d: %d\n", Case, ans);
    }
    return 0;
}
