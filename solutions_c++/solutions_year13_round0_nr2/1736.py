#include <cstdio>

using namespace std;

typedef int lawn[128][128];

bool check(lawn a, int N, int M) {
    for (int n = 0; n < N; ++n) for (int m = 0; m < M; ++m) {
        bool good = true;
        for (int nn = 0; good && nn < N; ++nn) good = a[nn][m] <= a[n][m];
        if (good) continue;

        good = true;
        for (int mm = 0; good && mm < M; ++mm) good = a[n][mm] <= a[n][m];
        if (!good) return false;
    }

    return true;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        int N, M;
        scanf("%d%d", &N, &M);

        lawn a;
        for (int n = 0; n < N; ++n) for (int m = 0; m < M; ++m) scanf("%d", &a[n][m]);

        printf("Case #%d: %s\n", t, check(a, N, M) ? "YES" : "NO");
    }

    return 0;
}
