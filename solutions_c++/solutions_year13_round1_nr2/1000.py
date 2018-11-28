#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 10

int T, E, R, N, v[MAXN];
int best;

void solve(int e, int i, int val) {
    if (i == N) {
        best = max(best, val);
        return;
    }

    for (int j = 0; j <= e; j++)
        solve(min(E, e-j+R), i+1, val+v[i]*j);
}

int main() {
    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        scanf("%d %d %d", &E, &R, &N);
        for (int i = 0; i < N; i++)
            scanf("%d", &v[i]);

        best = 0;
        solve(E, 0, 0);
        printf("Case #%d: %d\n", c, best);
    }
}
