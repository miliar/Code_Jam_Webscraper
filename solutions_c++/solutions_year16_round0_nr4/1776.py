#include <cstdio>
#include <algorithm>

using namespace std;

int T, K, C, S;

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d", &K, &C, &S);
        printf("Case #%d:", t);
        if (C == 1 || K == 1) {
            if (S == K) {
                for (int i = 1; i <= S; i++) {
                    printf(" %d", i);
                }
                printf("\n");
            } else {
                printf(" IMPOSSIBLE\n");
            }
        } else if (S >= K - 1) {
            for (int i = 2; i <= K; i++) {
                printf(" %d", i);
            }
            printf("\n");
        } else {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;

}
