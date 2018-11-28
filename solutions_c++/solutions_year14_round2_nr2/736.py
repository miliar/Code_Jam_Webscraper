#include <cstdio>
#include <algorithm>
using namespace std;

int A, B, K;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d %d", &A, &B, &K);
        int ans = 0;
        for (int i = 0; i < A; ++i)
            for (int j = 0; j < B; ++j)
                if ((i & j) < K)
                    ++ans;
        printf("Case #%d: %d\n", t, ans);
    }
}
