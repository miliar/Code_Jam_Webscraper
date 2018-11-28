#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int maxN = 1111;

int T, n, k;

int a[maxN], b[maxN], p[maxN], ans;

char S[maxN];

int main() {
#ifdef RS16
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif // RS16

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        scanf("%s%d", S, &k);
        n = strlen(S);

        ans = 0;
        for(int i = 0; i < n; ++i) {
            b[i] = !(a[i] = (S[i]=='+'));
            p[i] = b[i];
            for(int j = 1; j < k; ++j) {
                if(i-j < 0) break;
                p[i] ^= p[i-j];
            }

            if(p[i]) {
                ++ans;
                if(i+k > n) {
                    ans = -1; break;
                }
            }
        }

        printf("Case #%d: ", t);
        if(~ans) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}
