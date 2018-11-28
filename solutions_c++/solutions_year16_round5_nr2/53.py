#include <bits/stdc++.h>
using namespace std;

vector<int> g[110];
char s[110], nows[110];
char ask[110][110];
int num[100];

int q[110];
int deg[110], pre[110];
set<string> curs;
int sz[110];

void dfs(int u) {
    sz[u] = 1;
    for (auto &v : g[u]) {
        dfs(v);
        sz[u] += sz[v];
    }
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        fprintf(stderr, "cas = %d\n", cas);
        int n;
        scanf("%d", &n);
        for (int i = 0; i <= n; i++) {
            g[i].clear();
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &pre[i]);
            g[pre[i]].push_back(i + 1);
        }
        dfs(0);
        scanf("%s", s + 1);
        int m;
        scanf("%d", &m);
        for (int i = 0; i < m; i++) {
            scanf("%s", ask[i]);
            num[i] = 0;
        }
        int MAXCNT = 100000;
        curs.clear();
        for (int i = 0; i < MAXCNT; i++) {
            memset(deg, 0, sizeof(deg));
            for (int j = 0; j <= n; j++) {
                for (auto &v : g[j]) {
                    deg[v]++;
                }
            }
            int head = 0, tail = 0;
            q[tail++] = 0;
            int cnt = 0;
            for (int i = 0; i <= n; i++) {
                int tot = 0;
                for (int i = head; i < tail; i++) {
                    tot += sz[q[i]];
                }
                int x = rand() % tot + 1;
                for (int i = head; i < tail; i++) {
                    if (x <= sz[q[i]]) {
                        swap(q[i], q[head]);
                        break;
                    } else {
                        x -= sz[q[i]];
                    }
                }
                int id = q[head++];
                if (id != 0) {
                    nows[cnt++] = s[id];
                }
                for (auto &v : g[id]) {
                    deg[v]--;
                    if (deg[v] == 0) {
                        q[tail++] = v;
                    }
                }
            }
            nows[cnt] = 0;
            for (int i = 0; i < m; i++) {
                if (strstr(nows, ask[i]) != NULL) {
                    num[i]++;
                }
            }
        }
        printf("Case #%d:", cas);
        for (int i = 0; i < m; i++) {
            printf(" %.20f", num[i] * 1.0 / MAXCNT);
        }
        puts("");
    }
    return 0;
}