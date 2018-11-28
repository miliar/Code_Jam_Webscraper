#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long LL;

struct edge {
    int s, d;
}e[1048576];

int lst[1048576];
int T, n, D, gs;
int s[1048576];
int m[1048576];
int mi[1<<20];
int ma[1<<20];
int lid[1<<20];
int rid[1<<20];
int ap[1<<20];
LL S0, As, Cs, Rs;
LL M0, Am, Cm, Rm;

void addedge(int x, int y) {
    e[++gs].d = y;
    e[gs].s = lst[x];
    lst[x] = gs;
}

void dfs(int x, int Mi, int Ma) {
    mi[x] = Mi = min(Mi, s[x]);
    ma[x] = Ma = max(Ma, s[x]);
    for (int i = lst[x]; i != 0; i = e[i].s)
        dfs(e[i].d, Mi, Ma);
}

bool cmp1(int x, int y) {
    if (mi[x] != mi[y])
        return mi[x] < mi[y];
    return ma[x] < ma[y];
}

bool cmp2(int x, int y) {
    if (ma[x] != ma[y])
        return ma[x] < ma[y];
    return mi[x] < mi[y];
}

int main() {
    freopen("as.in", "r", stdin);
    freopen("as.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &D);
        scanf("%lld%lld%lld%lld", &S0, &As, &Cs, &Rs);
        scanf("%lld%lld%lld%lld", &M0, &Am, &Cm, &Rm);
        s[0] = S0;
        lid[0] = rid[0] = 0;
        for (int i = 1; i < n; ++i) {
            S0 = (S0 * As + Cs) % Rs;
            M0 = (M0 * Am + Cm) % Rm;
            s[i] = S0;
            m[i] = M0 % i;
            addedge(m[i], i);
            lid[i] = i;
            rid[i] = i;
        }
        dfs(0, 2147483647, -2147483648);
        sort(lid, lid + n, cmp1);
        sort(rid, rid + n, cmp2);
        int nr = n - 1;
        int now = 0;
        int ans = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (ma[lid[i]] - mi[lid[i]] <= D) {
                now += 1 - ap[lid[i]];
                ap[lid[i]] = 1;
            }
            while (nr >= 0 && ma[rid[nr]] > mi[lid[i]] + D) {
                now -= ap[rid[nr]];
                ap[rid[nr]] = 0;
                nr --;
            }
            ans = max(ans, now);
        }
        printf("%d\n", ans);
        memset(lst, 0, n * 4);
        gs = 0;
        memset(ap, 0, n * 4);
    }
    return 0;
}