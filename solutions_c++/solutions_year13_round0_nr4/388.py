#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>

#define MAX 21

using namespace std;

int dp[MAX][1 << MAX], ans[MAX][1 << MAX], req[MAX];
map<int, int> cnt[MAX], sum;

int dfs(int n, int x, int y) {
    int i, j, cur;
    map<int, int>::iterator it;

    if (y == (1 << n) - 1) return 1;
    if (~dp[x][y]) return dp[x][y];
    for (i = 0; i < n; ++i) {
        if (!(y & (1 << i)) && sum[req[i]]) {
            --sum[req[i]];
            for (it = cnt[i].begin(); it != cnt[i].end(); ++it) sum[it->first] += it->second;
            cur = dfs(n, i, y | (1 << i));
            for (it = cnt[i].begin(); it != cnt[i].end(); ++it) sum[it->first] -= it->second;
            ++sum[req[i]];
            if (cur) {
                ans[x][y] = i;
                return dp[x][y] = 1;
            }
        }
    }

    return dp[x][y] = 0;
}

int main() {
    int t, ct = 0, n, k, a, b, i, j, cur, nxt;
    map<int, int>::iterator it;

    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        sum.clear();
        for (i = 0; i < n; ++i) cnt[i].clear();

        scanf("%d %d", &k, &n);
        for (i = 0; i < k; ++i) {
            scanf("%d", &a);
            it = sum.find(a - 1);
            if (it != sum.end()) ++it->second;
            else sum.insert(make_pair(a - 1, 1));
        }
        for (i = 0; i < n; ++i) {
            scanf("%d %d", &req[i], &a);
            --req[i];
            if (sum.find(req[i]) == sum.end()) sum.insert(make_pair(req[i], 0));
            for (j = 0; j < a; ++j) {
                scanf("%d", &b);
                it = cnt[i].find(b - 1);
                if (it != cnt[i].end()) ++it->second;
                else cnt[i].insert(make_pair(b - 1, 1));
            }
        }

        printf("Case #%d: ", ++ct);
        memset(dp, -1, sizeof(dp));
        if (!dfs(n, n, 0)) printf("IMPOSSIBLE\n");
        else {
            for (cur = 0, i = n; cur != (1 << n) - 1; cur = nxt) {
                i = ans[i][cur]; nxt = cur | (1 << i);
                printf("%d", i + 1);
                putchar(nxt == ((1 << n) - 1) ? '\n' : ' ');
            }
        }
    }

    return 0;
}
