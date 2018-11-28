#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctype.h>
#include <limits.h>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <stack>
#include <set>
#include <bitset>
#define CLR(a) memset(a, 0, sizeof(a))
#define REP(i, a, b) for(ll i = a;i < b;i++)
#define REP_D(i, a, b) for(ll i = a;i <= b;i++)

typedef long long ll;

using namespace std;

const ll maxn = 1e6 + 100;
ll n, d, s0, as, cs, rs, m0, am, cm, rm;
ll s[maxn], m[maxn], vis[maxn];
vector<ll> G[maxn];
vector<ll> cnt[maxn];
ll ans;
ll min_s;
ll max_s;
void dfs_zeng(ll u, ll l, ll r)
{
    if(vis[u])
    {
        return;
    }
    if(s[u] >= l && s[u] <= r)
    {
        vis[u] = 1;
        ans++;
        REP(i, 0, G[u].size())
        {
            ll v = G[u][i];
            dfs_zeng(v, l, r);
        }
    }
    else
    {
        ;
    }
}
void dfs_jian(ll u)
{
    if(vis[u]==0)
    {
        return;
    }
    else
    {
        vis[u] = 0;
        ans--;
        REP(i, 0, G[u].size())
        {
            ll v = G[u][i];
            dfs_jian(v);
        }
    }
}

void solve()
{
    ll res = 0;
    ll l = min_s, r = min_s + d;
    CLR(vis);
    ans = 0;
    dfs_zeng(0, l, r);
    res = ans;
    for(ll i = 1;i <= max_s - d;i++)
    {
        l = i;
        r = i + d;
        //if(cnt[r].size() > cnt[l - 1].size())
        //{
            REP(j, 0, cnt[l-1].size())
            {
                ll v = cnt[l-1][j];
                dfs_jian(v);
            }
            REP(j, 0, cnt[r].size())
            {
                ll v = cnt[r][j];
                if(vis[m[v]] || v == 0)
                {
                    dfs_zeng(v, l, r);
                }
            }
            res = max(res, ans);
        //}
    }
    printf("%lld\n", res);
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("1Aoutnew.txt", "w", stdout);
    ll ncase;
    scanf("%lld", &ncase);
    REP_D(_, 1, ncase)
    {
        printf("Case #%lld: ", _);
        scanf("%lld%lld", &n, &d);
        scanf("%lld%lld%lld%lld", &s0, &as, &cs, &rs);
        scanf("%lld%lld%lld%lld", &m0, &am, &cm, &rm);
        for(ll i = 0;i <= 1000000;i++)
        {
            G[i].clear();
            cnt[i].clear();
        }
        s[0] = s0;
        m[0] = m0;
        min_s = s0;
        max_s = s0;
        cnt[s0].push_back(0);
        REP_D(i, 1, n - 1)
        {
            s[i] = (s[i-1]*as+cs)%rs;
            cnt[s[i]].push_back(i);
            m[i] = (m[i-1]*am+cm)%rm;
            //G[m[i]].push_back(i);
            min_s = min(min_s, s[i]);
            max_s = max(max_s, s[i]);
            //printf("----s i is %d  s is %d  fa is %d\n", i, s[i], m[i]);
        }
        REP_D(i, 1, n - 1)
        {
            //s[i] = (s[i-1]*as+cs)%rs;
            //cnt[s[i]].push_back(i);
            m[i] = m[i]%i;
            G[m[i]].push_back(i);
            //min_s = min(min_s, s[i]);
            //max_s = max(max_s, s[i]);
            //printf("s i is %d  fa is %d\n", i, m[i]);
        }
        solve();
    }
    return 0;
}
