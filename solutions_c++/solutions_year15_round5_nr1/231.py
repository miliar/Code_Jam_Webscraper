#include <bits/stdc++.h>

typedef long long int64;
#define sz(A) (int((A).size()))

using namespace std;

void dfs(int u, vector <vector <int> > &G, vector <int> &cnt, vector <int> &res, int &rescnt, int color)
{
    if (cnt[u])
    {
        rescnt += color - res[u];
        res[u] = color;

        for (int to: G[u])
        {
            dfs(to, G, cnt, res, rescnt, color);
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++)
    {
        int n, d;
        cin >> n >> d;
        int s0, as, cs, rs;
        cin >> s0 >> as >> cs >> rs;
        int m0, am, cm, rm;
        cin >> m0 >> am >> cm >> rm;

        vector <vector <int> > G(n);
        vector <int> prev(n);
        vector <pair <int, int> > A(n);
        A[0].first = s0;

        for (int i = 1; i < n; i++)
        {
            s0 = (int64(s0) * as + cs) % rs;
            m0 = (int64(m0) * am + cm) % rm;
            A[i].first = s0;
            A[i].second = i;
            G[m0 % i].push_back(i);
            prev[i] = m0 % i;
        }
        sort(A.begin(), A.end());
        vector <int> cnt(n), res(n);

        int pos = 0, rescnt = 0, ans = 0;

        while (pos < n && A[pos].first - A[0].first <= d)
        {
            cnt[A[pos].second] = 1;
            pos++;
        }

        if (cnt[0] == 1)
        {
            dfs(0, G, cnt, res, rescnt, 1);
            ans = max(ans, rescnt);
        }

        for (int i = 1; i < n; i++)
        {
            dfs(A[i - 1].second, G, cnt, res, rescnt, 0);
            cnt[A[i - 1].second] = 0;
            vector <int> now;

            while (pos < n && A[pos].first - A[i].first <= d)
            {
                cnt[A[pos].second] = 1;
                now.push_back(A[pos].second);
                pos++;
            }
            sort(now.begin(), now.end());

            for (auto x: now)
            {
                if (x == 0 || res[prev[x]] == 1)
                    dfs(x, G, cnt, res, rescnt, 1);
            }

            if (cnt[0] == 1)
                ans = max(ans, rescnt);
        }
        cout << "Case #" << tst + 1 << ": " << ans << '\n';
    }

    return 0;
}
