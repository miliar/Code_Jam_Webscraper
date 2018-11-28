#include <cstdio>

bool v[11];
int cs, n, mx, ans, a[11], b[11], c[11];

void dfs(int dep, bool got) {
    if (dep == n) {
        int tmp = 0;
        for (int i = 0; i < n; ++i)
            c[b[i]] = i;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (c[i] > c[j])
                    ++tmp;
        if (tmp < ans)
            ans = tmp;
        return;
    }
    for (int i = 0; i < n; ++i)
        if (!v[i] && (!dep || dep && (got && a[i] < a[b[dep - 1]] || !got && a[i] > a[b[dep - 1]]))) {
            v[b[dep] = i] = true;
            dfs(dep + 1, got || a[i] == mx);
            v[i] = false;
        }
}

inline void work() {
    scanf("%d", &n);
    for (int i = mx = 0; i < n; ++i) {
        scanf("%d", &a[i]);
        if (a[i] > mx)
            mx = a[i];
    }
    ans = 1000000000;
    dfs(0, false);
    printf("Case #%d: %d\n", ++cs, ans);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
