#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <sstream>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const long double eps = 1e-10;

const int N = 1000005;

int s[N], m[N], fa[N], cnt[N], f[N];
vector<int> edge[N];

void work()
{
    int n, D, as, cs, rs, am, cm, rm;
    cin >> n >> D;
    cin >> s[0] >> as >> cs >> rs;
    cin >> m[0] >> am >> cm >> rm;
    for (int i = 0; i < n; ++i)
    {
        edge[i].clear();
        f[i] = 0;
        cnt[i] = 0;
    }
    for (int i = 1; i < n; ++i)
    {
        s[i] = (1LL * s[i - 1] * as + cs) % rs;
        m[i] = (1LL * m[i - 1] * am + cm) % rm;
        fa[i] = m[i] % i;
        edge[m[i] % i].pb(i);
    }
    vector<pair<int, int> > a;
    for (int i = 0; i < n; ++i)
        a.pb(mp(s[i], i));
    sort(a.begin(), a.end());
    int ans = 1;
    for (int l = 0, r = -1; l < n;)
    {
        while (r + 1 < n && a[r + 1].first - a[l].first <= D)
        {
            ++r;
            int i = a[r].second;
            ++cnt[i];
            for (int j = 0; j < sz(edge[i]); ++j)
            {
                int k = edge[i][j];
                f[i] += f[k];
            }
            ++f[i];
            int k = i;
            while (1)
            {
                if (k == 0) break;
                k = fa[k];
                if (!cnt[k]) break;
                f[k] += f[i];
            }
        }
        if (cnt[0]) ans = max(ans, f[0]);

        int i = a[l].second;
        --cnt[i];
        int k = i;
        while (1)
        {
            if (k == 0) break;
            k = fa[k];
            if (!cnt[k]) break;
            f[k] -= f[i];
        }
        f[i] = 0;
        ++l;
    }
    cout << ans << endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ": ";
        work();
    }
    return 0;
}
