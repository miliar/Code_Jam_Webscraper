#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
using namespace std;

int n, k;
int a[45];
int need[25];
int T;
int p[25];
int q[25][45];
int b[1048577];

bool dfs(int x) {
    int& ret = b[x];
    if (ret != -1)
        return ret;
    ret = 0;
    int tot[45] = {0};
    memcpy(tot, a, sizeof(tot));
    for (int i = 0; i < n; ++i) {
        if ((1 << i) & x) {
            --tot[need[i]];
            for (int j = 0; j < p[i]; ++j) {
                ++tot[q[i][j]];
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        if ((((1 << i) & x) == 0) && (tot[need[i]] > 0)) {
            if (dfs(x | (1 << i))) {
                ret = 1;
                return ret;
            }
        }
    }
    return ret;
}

int x;

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        memset(a, 0, sizeof(a));
        memset(b, -1, sizeof(b));
        scanf("%d%d", &k, &n);
        b[(1 << n) - 1] = 1;
        for (int i = 0; i < k; ++i) {
            scanf("%d", &x);
            ++a[x];
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", &need[i]);
            scanf("%d", &p[i]);
            for (int j = 0; j < p[i]; ++j) {
                scanf("%d", &q[i][j]);
            }
        }
        printf("Case #%d:", test);
        fprintf(stderr, "%d\n", test);
        bool ans = dfs(0);
        if (!ans) {
            puts(" IMPOSSIBLE");
        } else {
            int now = 0;
            while(now + 1 != (1 << n)) {
                for (int i = 0; i < n; ++i) {
                    if (((1 << i) & now) == 0) {
                        if (b[now | (1 << i)] == 1) {
                            printf(" %d", i + 1);
                            now |= (1 << i);
                            break;
                        }
                    }
                }
            }
            puts("");
        }
    }
    return 0;
}

