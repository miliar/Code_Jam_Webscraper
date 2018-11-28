#include <cstdio>
using namespace std;

int main() {
    int T, A, B, K;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d", &A, &B, &K);
        int cnt = 0;
        for (int i = 0; i < A; i++)
            for (int j = 0; j < B; j++)
                if ((i & j) < K)
                    cnt++;
        printf("Case #%d: %d\n", t, cnt);
    }
}
