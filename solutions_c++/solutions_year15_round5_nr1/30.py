#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
using namespace std;

const int N = 1000500;

vector<int> S, M, par;
vector<int> E[N];

vector<int> alive, connected;

int DFS(int x, int l, int r) {
    if (S[x] < l || S[x] > r)
        return 0;
    int ans = 1;
    for (int y : E[x])
        ans += DFS(y, l, r);
    return ans;
}

int cur_ans = 0;

void DFS_add(int x) {
    if (!alive[x])
        return;
    assert(!connected[x]);
    connected[x] = true;
    cur_ans++;
    for (int y : E[x])
        DFS_add(y);
}

void add(int x) {
    alive[x] = true;
    if (x == 0 || connected[par[x]]) {
        DFS_add(x);
    }
}

void DFS_del(int x) {
    if (!alive[x])
        return;
    cur_ans--;
    connected[x] = false;
    for (int y : E[x])
        DFS_del(y);
}

void rem(int x) {
    if (connected[x])
        DFS_del(x);
    alive[x] = false;
}

void solve(int cs_num) {
    int n, d;
    scanf("%d %d", &n, &d);
    int s0, as, cs, rs;
    scanf("%d %d %d %d", &s0, &as, &cs, &rs);
    int m0, am, cm, rm;
    scanf("%d %d %d %d", &m0, &am, &cm, &rm);
    S.resize(n);
    M.resize(n);
    par.resize(n);
    S[0] = s0;
    M[0] = m0;
    for (int i = 1; i < n; i++) {
        S[i] = (S[i - 1] * 1ll * as + cs) % rs;
        M[i] = (M[i - 1] * 1ll * am + cm) % rm;
        par[i] = M[i] % i;
    }
    for (int i = 0; i < n; i++)
        E[i].clear();    
    for (int i = 1; i < n; i++)
        E[M[i] % i].push_back(i);
    vector<pair<int, int> > sal;
    for (int i = 0; i < n; i++)
        sal.push_back(make_pair(S[i], i));
    sort(sal.begin(), sal.end());

    alive.clear();
    alive.resize(n, 0);
    connected.clear();
    connected.resize(n, 0);


    cur_ans = 0;
    int ans = 0;

    int l = 0, r = 0;
    while (l != n) {
        while (r != n && sal[r].first - sal[l].first <= d) {
            add(sal[r].second);
            ans = max(ans, cur_ans);
            r++;
        }
        rem(sal[l].second);
        l++;
    }

    printf("Case #%d: %d\n", cs_num, ans);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
        fflush(stdout);
    }
}
