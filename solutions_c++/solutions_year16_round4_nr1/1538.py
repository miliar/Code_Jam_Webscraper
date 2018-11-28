#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 12;

int ans[(1<<MAXN) * 2 + 10];

int winner[3][3] = {
    {-1, 0, 2},
    {0, -1, 1},
    {2, 1, -1}
};

int N;

bool check() {
    for (int i = 0, j = N; i+1 < j; i += 2, ++j) {
        if (ans[i] == ans[i+1]) return false;
        ans[j] = winner[ans[i]][ans[i+1]];
    }

    const char* m = "PRS";
    for (int i = 0; i < N; ++i)
        putchar(m[ans[i]]);
    putchar('\n');
    return true;
}

int cnt[3];
bool dfs(int i) {
    if (i == N) {
        return check();
    }

    for (int v = 0; v < 3; ++v) {
        if (cnt[v]) {
            ans[i] = v;
            cnt[v] -= 1;
            if (dfs(i+1)) return true;
            cnt[v] += 1;
        }
    }

    return false;
}

void solve() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 3; ++i) scanf("%d", &cnt[i]);
    swap(cnt[0], cnt[1]);

    N = 1<<n;

    if (not dfs(0))
        puts("IMPOSSIBLE");
}

int main() {
    int T; scanf("%d", &T); for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);

        solve();
    }

    return 0;
}
