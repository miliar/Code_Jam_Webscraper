#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<ctime>
#include<queue>
#include<utility>
#include<climits>

using namespace std;

#define mcpy(from, to) memcpy((to),(from),sizeof((from)))
#define msetz(pp) memset((pp),0,sizeof((pp)))
#define mseto(pp) memset((pp),1,sizeof((pp)))
#define msetno(pp) memset((pp),-1,sizeof((pp)))
#define mseti(pp) memset((pp),0x3f3f3f3f,sizeof((pp)))
#define msetni(pp) memset((pp),0xc0c0c0c0,sizeof((pp)))
typedef pair<int, int> PII;
//typedef __int64 LL;
typedef long long LL;
const int INF = 0x3f3f3f3f;
const LL LINF = 1ll << 60;
const double inf = 1e20, eps = 1e-8;

int ceil(int aa, int bb) {
    if (bb < 0) {
        aa = -aa;
        bb = -bb;
    }
    if (aa > 0) return (aa - 1) / bb + 1;
    else return aa / bb;
}

int floor(int aa, int bb) {
    if (bb < 0) {
        aa = -aa;
        bb = -bb;
    }
    if (aa >= 0) return aa / bb;
    else return (aa + 1) / bb - 1;
}

void readint(int &x) {
    char c;
    while (c = getchar(), (c < '0' || c > '9') && (c != '-'));
    bool flag = (c == '-');
    if (flag) c = getchar();
    x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + c - 48;
        c = getchar();
    }
    if (flag) x = -x;
}

void readLL(LL &x) {
    char c;
    while (c = getchar(), (c < '0' || c > '9') && (c != '-'));
    bool flag = (c == '-');
    if (flag) c = getchar();
    x = 0ll;
    while (c >= '0' && c <= '9') {
        x = x * 10ll + LL(c - 48);
        c = getchar();
    }
    if (flag) x = -x;
}

void putint(int x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    int len = 0, data[10];
    while (x) {
        data[len++] = x % 10;
        x /= 10;
    }
    if (!len) data[len++] = 0;
    while (len--) putchar(data[len] + 48);
    putchar('\n');
}

void putLL(LL x) {
    if (x < 0ll) {
        putchar('-');
        x = -x;
    }
    int len = 0, data[30];
    while (x > 0ll) {
        data[len++] = x % 10ll;
        x /= 10ll;
    }
    if (!len) data[len++] = 0;
    while (len--) putchar(data[len] + 48);
    putchar('\n');
}

const int MAXN = 1005;
int to[MAXN], dep[MAXN];
vector<int> pre[MAXN];
int n, ans1, ans2;
int vis[MAXN], dis[MAXN];

void bfs(int x) {
    int s = x;
    queue<int>q;
    q.push(x);
    vis[x] = true;
    bool inq[MAXN];
    msetz(inq);
    while (!q.empty()) {
        x = q.front();  q.pop();
        int y = to[x];
        if (dis[y])  continue;
        inq[y] = true;
        if (!vis[y]) {
            vis[y] = true;
            q.push(y);
        }
    }
    dis[s] = 1;
    q.push(s);
    while (!q.empty()) {
        x = q.front();  q.pop();
        int y = to[x];
        if (!inq[y]) continue;
        if (dis[y] == 0) {
            dis[y] = dis[x] + 1;
            q.push(y);
        }
        else {
            ans1 = max(ans1, dis[x] - dis[y] + 1);
        }
    }
}

int find(int x, int fa) {
    int ans = 0;
    for (auto v : pre[x]) {
        if (v == fa) continue;
        ans = max(ans, find(v, x));
    }
    return ans + 1;
}

int main() {
    int TT;
    freopen("C-large.in", "r", stdin);
    freopen("hahalarge.out", "w", stdout);
    readint(TT);
    for (int TTT = 1; TTT <= TT; TTT++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) pre[i].clear();
        for (int i = 1; i <= n; i++) {
            scanf("%d", &to[i]);
            pre[to[i]].push_back(i);
        }
        ans1 = 0;
        ans2 = 0;
        msetz(vis);
        msetz(dis);
        for (int i = 1; i <= n; i++) if (!vis[i]) bfs(i);
        msetz(dep);
        for (int i = 1; i <= n; i++) if (dep[i] == 0 && to[to[i]] == i) {
            dep[i] = dep[to[i]] = 1;
            int left = find(i, to[i]), right = find(to[i], i);
            ans2 += left + right;
        }
        printf("Case #%d: %d\n", TTT, max(ans1, ans2));
    }
    return 0;
}