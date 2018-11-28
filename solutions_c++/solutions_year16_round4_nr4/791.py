#include <stdio.h>
#include <vector>
#include <algorithm>
#define pb push_back
#define MAXN 5
#define INF 0x3f3f3f3f
using namespace std;

char can[2 * MAXN][2 * MAXN];
char mat[2 * MAXN][2 * MAXN];
int n;
int res;
int good;

vector <int> v;
int used[5];

void solve2(int pos) {
    if (pos >= n) {
        return;
    }
    int done = 0;
    for (int i = 0; i < n; i++) {
        if (mat[v[pos]][i] == '1' && !used[i]) {
            used[i] = 1;
            done = 1;
            solve2(pos + 1);
            used[i] = 0;
        }
    }
    if (done == 0) {
        good = 0;
    }
    return;
}

int check2(void) {
    good = 1;
    for (int i = 0; i < n; i++) {
        used[i] = 0;
    }

    /*printf("here check2\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    printf("\n"); */
    solve2(0);
    return good;
}

int check(void) {
    v.clear();
    for (int i = 0; i < n; i++) {
        v.pb(i);
    }

    int ok = 1;
    do {
        if (!check2()) {
            ok = 0;
            break;
        }
    }while(next_permutation(v.begin(), v.end()));
    return ok;
}

int solve(void) {
    int res = INF;
    for (int mask = 0; mask < 1 << (n * n); mask++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = can[i][j];
            }
        }

        int cost = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int bit = (mask >> (i * n + j)) & 1;
                if (bit) {
                    cost++;
                    mat[i][j] = '1';
                }
            }
        }

        /*printf("debug, mask = %d, cost = %d\n", mask, cost);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                printf("%c", mat[i][j]);
            }
            printf("\n");
        }
        printf("\n"); */
        if (check()) {
            //printf("here mask = %d, cost = %d\n", mask, cost);
            res = min(res, cost);
        }
    }
    return res;
}

int main(void) {
    int t;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d", &n);
        for (int i = 0; i < n; i++) {
            scanf(" %s", can[i]);
        }

        int res = solve();
        printf("Case #%d: %d\n", caso, res);
    }
    return 0;
}
