#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000002013

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int T, N, M, o, e, p;

inline ll rangeCost(ll lft, ll rgt)
{
    return  ((rgt - lft + 1) * (2*N - rgt + lft) / 2) % MOD;
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> N >> M;
        vector<pll> events;
        ll cost1 = 0, cost2 = 0;
        for (int i = 0; i < M; ++i)
        {
            cin >> o >> e >> p;
            events.push_back(pll(o, -p));
            events.push_back(pll(e, p));
            cost1 += p*rangeCost(o, e);
            cost1 %= MOD;
        }
        sort(events.begin(), events.end());
        stack<pll> tix;
        for (int i = 0; i < events.size(); ++i)
        {
            o = e = events[i].first, p = events[i].second;
            if (p < 0)
            {
                tix.push(pll(o, -p));
            }
            else
            {
                while (p)
                {
                    if (p < tix.top().second)
                    {
                        tix.top().second -= p;
                        cost2 += p*rangeCost(tix.top().first, e);
                        p = 0;
                    }
                    else
                    {
                        p -= tix.top().second;
                        cost2 += tix.top().second*rangeCost(tix.top().first, e);
                        tix.pop();
                    }
                    cost2 %= MOD;
                }
            }
        }
        ll ans = (cost1 - cost2 + MOD) % MOD;
        cout << "Case #" << z << ": " << ans << endl;
    }
}
