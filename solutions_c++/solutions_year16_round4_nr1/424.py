#include <stdio.h>
#include <algorithm>

using namespace std;

void dfs(int n, int p, int r, int s) {
    if (n == 0) {
        if (p) {
            printf("P");
        } else if (r) {
            printf("R");
        } else if (s) {
            printf("S");
        }
        return;
    }

    if (p % 2 == 0) {
        dfs (n - 1, p / 2, r / 2 + 1, s / 2);
        dfs (n - 1, p / 2, r / 2, s / 2 + 1);
    } else {
        dfs (n - 1, p / 2 + 1, r / 2, s / 2);
        dfs (n - 1, p / 2, (r + 1) / 2, (s + 1) / 2);
    }
}

int main() {
    int T;
    scanf( "%d", &T );
    for (int test = 1; test <= T; test ++) {
        int N, R, P, S;
        scanf( "%d %d %d %d", &N, &R, &P, &S );
        printf( "Case #%d: ", test );
        int mx = max(max(R, P), S);
        int mn = min(min(R, P), S);

        if (mx - mn > 1) {
            printf( "IMPOSSIBLE\n" );
        } else {
            dfs(N, P, R, S);
            printf( "\n" );
        }
    }

    return 0;
}
