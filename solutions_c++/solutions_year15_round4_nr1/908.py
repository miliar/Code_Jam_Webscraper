#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define esp 1e-14
#define lson   l, m, rt<<1
#define rson   m+1, r, rt<<1|1
#define sz(x) ((int)((x).size()))
#define pf(x) ((x)*(x))
#define pb push_back
#define pi acos(-1.0)
#define in freopen("A-large.in", "r", stdin);
#define IN freopen("solve_in.txt", "r", stdin);
#define out freopen("solve_out.txt", "w", stdout);
#define bug(x) printf("Line : %u >>>>>>\n", (x));
#define TL cerr << "Time elapsed: " << (double)clock() / CLOCKS_PER_SEC * 1000 << " ms" << endl;
#define inf 0x0f0f0f0f
using namespace std;
typedef long long LL;
typedef unsigned US;
typedef pair<int, int> PII;
typedef map<PII, int> MPS;
typedef MPS::iterator IT;

const int maxn = 110;
char maze[maxn][maxn];
int num[maxn][maxn];
vector<int>g[maxn*maxn], G[maxn*maxn];

int cnt;
int n, m;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
bitset<maxn*maxn>  Cir;
int vis[maxn*maxn];

bool cango(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int id(char ch) {
    if (ch == '^') return 3;
    if (ch == 'v') return 2;
    if (ch == '>') return 0;
    return 1;
}
int id(int x, int y) {
    if (num[x][y] == -1) {
        num[x][y] = cnt++;
    }
    return num[x][y];
}
void dfs(int x) {
    vis[x] = 1;
    for (int i = 0; i < (int)g[x].size(); i++) {
        int y = g[x][i];
        if (!vis[y]) {
            dfs(y);
        } else if (vis[y] == 1) {
            Cir[y] = true;
        }
    }
    vis[x] = 2;
}
int main () {
//    in
//    out
//IN
    int T;
    for (int t = scanf("%d", &T); t <= T; t++) {
        for (int i = 0; i < maxn*maxn; i++)
            g[i].clear(), G[i].clear();
        cnt = 0;
        memset(num, -1, sizeof num);

        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", maze[i]);
        }
        bool ok = true;
        for (int i = 0; i < n && ok; i++)
            for (int j = 0; j < m && ok; j++) {
                if (maze[i][j] == '.') continue;
                id(i, j);
                int k = id(maze[i][j]);
                int ct = 0;
                for (int kk = 0; kk < 4; kk++) {
                    int x = i, y = j;
                    for (int s = 0; s < max(n, m); s++) {
                        x = x + dx[kk];
                        y = y + dy[kk];
                        if (!cango(x, y)) break;
                        if (maze[x][y] == '.') continue;
                        ct++;
                        if (kk == k) {
                            int u = id(i, j);
                            int v = id(x, y);
                            g[u].push_back(v);
                            G[v].push_back(u);
                        }
                        break;
                    }
                }
                if (ct == 0) {
                    ok = false;
                    break;
                }
            }
//            cout << cnt << endl;
        if (!ok) {
            printf("Case #%d: %s\n", t, "IMPOSSIBLE");
            continue;
        }
        memset(vis, 0, sizeof vis);
        Cir.reset();
        for (int i = 0; i < cnt; i++) {
            if (vis[i]) continue;
            dfs(i);
        }
        queue<int> q;

        for (int i = 0; i < cnt; i++) {
            if (Cir[i]) {
                q.push(i);
            }
        }
        while (q.size()) {
            int u = q.front();
            q.pop();
            for (int i = 0; i < (int)G[u].size(); i++) {
                int v = G[u][i];
                if (Cir[v]) continue;
                Cir[v] = true;
                q.push(v);
            }
        }
        int ans = 0;
        for (int i = 0; i < cnt; i++) {
            if (!Cir[i] && (int)g[i].size() == 0)
                ans++;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
