#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T, ca = 1, K, C, S, i, j;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", ca++);
        if (C == 1) {
            for (i = 1;i <= K;i++) {
                printf(" %d", i);
            }
            puts("");
        }else {
            int a = K;
            for (i = 0;i < (K+1)/2;i++) {
                printf(" %d", a);
                a += K-1;
            }
            puts("");
        }
    }
}
