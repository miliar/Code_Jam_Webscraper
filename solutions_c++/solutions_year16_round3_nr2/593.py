#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 55;

int n;
ll m;
int e[maxN][maxN];
ll d1[maxN], d2[maxN];

void Update() {
    memset(d1, 0, sizeof d1);
    memset(d2, 0, sizeof d2);
    d1[1] = 1;
    for(int i = 2; i <= n; ++i)
        for(int j = 1; j < i; ++j)
            d1[i] += e[j][i] * d1[j];
    d2[n] = 1;
    for(int i = n - 1; i >= 1; --i)
        for(int j = n; j > i; --j)
            d2[i] += e[i][j] * d2[j];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int test = 1; test <= nTests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d %I64d", &n, &m);
        memset(e, 0, sizeof e);
        for(int i = 1; i <= n; ++i)
            for(int j = i + 1; j <= n; ++j) e[i][j] = 1;
        Update();
        ll mm = d1[n];
        m = mm - m;
        while (m > 0) {
            int u = 0, v = 0;
            bool ok = false;
            for(int i = 1; i <= n; ++i)
                for(int j = i + 1; j <= n; ++j) {
                    if (e[i][j] && d1[i] * d2[j] <= m && d1[i] * d2[j] > d1[u] * d2[v]) {
                        u = i; v = j;
                        ok = true;
                    }
                }
            if (!ok) break;
            m -= d1[u] * d2[v];
            e[u][v] = 0;
            Update();
        }
        if (m != 0) printf("IMPOSSIBLE\n");
        else {
            printf("POSSIBLE\n");
            for(int i = 1; i <= n; ++i) {
                for(int j = 1; j <= n; ++j) printf("%d",e[i][j]);
                printf("\n");
            }
        }
    }

    return 0;
}

