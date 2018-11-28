#include <bits/stdc++.h>
using namespace std;

int n;
int p[1001];
int c[1001];

int solve() {
    memset(c, 0, sizeof(c));
    int res = 1000;
    
    for (int mx = 1; mx <= 1000; mx++) {
        int moves = 0;
        for (int i = 0; i < n; i++) {
            if (p[i] > mx) {
                moves += (p[i] - 1) / mx;
            }
        }
        if (moves + mx < res) {
            //printf("better: %d, moves=%d, mx=%d\n", moves + mx, moves, mx);
            res = moves + mx;
        }
    }
    
    return res;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &p[i]);
        }
        
        printf("Case #%d: ", test);
        printf("%d", solve());
        printf("\n");
    }

    return 0;
}
