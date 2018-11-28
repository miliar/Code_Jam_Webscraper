#include <cstdio>

const int MAXN = 100;
const int MAXE = 10;

int e, r, n;
int v[MAXN];
int f[MAXE][MAXN];

int max(int a, int b) {
    return (a > b) ? a : b;
}

int min(int a, int b) {
    return (a < b) ? a : b;
}

void work() {
    for (int i = 0; i <= e; i++) {
        f[i][n - 1] = i * v[n - 1];
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j <= e; j++) {
            int maxg = 0;
            for (int k = 0; k <= j; k++) {
                int tmp = f[min(e, j - k + r)][i + 1] + k * v[i];
                if (tmp > maxg) maxg = tmp;
            }
            f[j][i] = maxg;
        }
    }
}

int main() {
    int t;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf("%d%d%d", &e, &r, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &v[i]);
        }
        work();
        printf("Case #%d: %d\n", tc, f[e][0]);
    }
    return 0;
}
