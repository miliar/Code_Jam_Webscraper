#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
const int MAXV = 30;
int C, D, V;
int num[MAXN];
bool vis[MAXN];
bool used[MAXN];
int b2[MAXN];
vector<int> ddd;
bool check()
{
    memset(vis, 0, sizeof(vis));
    int len = ddd.size();
    int bd = 1<<len;
    for (int i = 0; i < bd; ++i) {
        int t = 0;
        for (int j = 0; j < len; ++j) {
            if (i & (1<<j)) {
                t += ddd[j];
            }
        }
        vis[t] = true;
    }
    for (int i = 1; i <= V; ++i) {
        if (!vis[i]) {
            return false;
        }
    }
    return true;
}

int ans = 0;
void dfs(int dep, int last)
{
    if (0 == dep) {
        ddd.clear();
        for (int i = 0; i < D; ++i) {
            ddd.push_back(num[i]);
        }
    }
    if (check()) {
        ans = min(ans, dep);
    }
    if (5 <= dep) {
        return;
    }
    for (int i = last+1; i <= V; ++i) {
        if (used[i]) {
            continue;
        }
        ddd.push_back(i);
        dfs(dep+1, i);
        ddd.pop_back();
    }
}
int main(int argc, char *argv[])
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d%d", &C, &D, &V);
        cerr << C << ' ' << D << ' ' << V << endl;
        memset(used, 0, sizeof(used));
        for (int i = 0; i < D; ++i) {
            scanf("%d", num+i);
            used[num[i]] = true;
        }
        ans = 100;
        dfs(0, 0);
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
