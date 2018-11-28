#include <map>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;

typedef long long LL;

struct edge {
    int d, s;
    long long c;
}e[1<<21];

int T;
int n, m, wc, gs;
map <string, int> dict;
int g[256][4096];
char cent[1048576];
char word[16];
int lst[16384];
int d[16384];
int cur[16384];
queue <int> q;

void addEdge(int x, int y, int c) {
    e[++gs].d = y; e[gs].s = lst[x]; e[gs].c = c; lst[x] = gs;
    e[++gs].d = x; e[gs].s = lst[y]; e[gs].c = 0; lst[y] = gs;
}

int getword(string w) {
    if (dict[w] == 0)
        dict[w] = ++wc;
    return dict[w];
}

bool bfs() {
    memset(d, 255, sizeof(d));
    d[1] = 0;
    q.push(1);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (int i = lst[x]; i > 0; i = e[i].s)
            if (d[e[i].d] == -1 && e[i].c > 0) {
                d[e[i].d] = d[x] + 1;
                q.push(e[i].d);
            }
    }
    return d[2] != -1;
}

LL dfs(int x, int flow) {
    if (x == 2)
        return flow;
    LL ans = 0;
    int i;
    for (i = cur[x]; i > 0; i = e[i].s)
        if (e[i].c && d[x] + 1 == d[e[i].d]) {
            LL t = dfs(e[i].d, min((LL)flow, e[i].c));
            e[i].c -= t;
            e[i ^ 1].c += t;
            ans += t;
            flow -= t;
            if (flow == 0)
                break;
        }
    cur[x] = i;
    return ans;
}

LL dinic() {
    LL ans = 0;
    while (bfs()) {
        memcpy(cur, lst, sizeof(cur));
        ans += dfs(1, 0x7fffffff);
    }
    return ans;
}

int main() {
    freopen("cl.in", "r", stdin);
    freopen("cl.out", "w", stdout);
    scanf("%d\n", &T);
    for (int test = 1; test <= T; test ++) {
        memset(lst, 0, sizeof(lst));
        gs = 1;
        printf("Case #%d: ", test);
        memset(g, 0, sizeof(g));
        dict.clear();
        scanf("%d\n", &n);
        wc = 0;
        for (int i = 1; i <= n; i++) {
            gets(cent);
            char * p = cent;
            while (*p != 0) {
                sscanf(p, "%s", word);
                g[i][getword(string(word))] = 1;
                p += strlen(word);
                while (*p == ' ') p++;
            }
        }
        addEdge(1, 3, 1e9);
        addEdge(4, 2, 1e9);
        for (int i = 3; i <= n; i++) {
            addEdge(1, i + 2, 100000);
            addEdge(i + 2, 2, 100000);
        }
        for (int i = 1; i <= wc; i++) {
            addEdge(i * 2 + n + 1, i * 2 + n + 2, 1);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= wc; j++)
                if (g[i][j]) {
                    addEdge(i + 2, j * 2 + n + 1, 1e9);
                    addEdge(j * 2 + n + 2, i + 2, 1e9);
                }
        }
        printf("%d\n", (int)dinic() - (n - 2) * 100000);
    }
    return 0;
}