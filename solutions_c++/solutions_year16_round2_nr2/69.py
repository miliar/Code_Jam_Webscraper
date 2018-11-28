#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()

const ll inf = (ll)3e18;

ll min_diff (const string &fst, const string &snd)
{
    assert(sz(fst) == sz(snd));
    ll ans = inf;

    vector<ll> cost(sz(fst));
    cost.back() = 1;
    for (int i = sz(cost) - 2; i >= 0; i--)
        cost[i] = cost[i + 1] * 10LL;

    for (int it = 0; it <= sz(fst); it++)
    {
        bool ok = true;
        for (int i = 0; i < it; i++)
            ok &= (fst[i] == snd[i] || fst[i] == '?' || snd[i] == '?');
        if (!ok)    continue;
        if (it == sz(fst))  return 0;

        for (int f = 0; f <= 9; f++)
        if (fst[it] == '?' || fst[it] == '0' + f)
        for (int s = 0; s <= 9; s++)
        if (snd[it] == '?' || snd[it] == '0' + s)
        {
            if (s < f)
            {
                ll cur_diff = (f - s) * cost[it];
                for (int j = it + 1; j < sz(fst); j++)
                {
                    int dg_f = (fst[j] == '?' ? 0 : fst[j] - '0');
                    int dg_s = (snd[j] == '?' ? 9 : snd[j] - '0');
                    cur_diff += (dg_f - dg_s) * cost[j];
                }
                assert(cur_diff >= 0);
                ans = min(ans, cur_diff);
            }
            else if (s > f)
            {
                ll cur_diff = (s - f) * cost[it];
                for (int j = it + 1; j < sz(fst); j++)
                {
                    int dg_f = (fst[j] == '?' ? 9 : fst[j] - '0');
                    int dg_s = (snd[j] == '?' ? 0 : snd[j] - '0');
                    cur_diff += (dg_s - dg_f) * cost[j];
                }
                assert(cur_diff >= 0);
                ans = min(ans, cur_diff);
            }
        }
    }

    return ans;
}

void solve (string fst, int test)
{
    string snd;
    cin >> snd;

    ll res = min_diff(fst, snd);

    for (int i = 0; i < sz(fst); i++)
    {
        bool ok = false;
        char ch = fst[i];
        for (char j = '0'; j <= '9' && !ok; j++)
        if (ch == '?' || ch == j)
        {
            fst[i] = j;
            ll nres = min_diff(fst, snd);
            ok |= (res == nres);
        }
        assert(ok);
    }

    for (int i = 0; i < sz(snd); i++)
    {
        bool ok = false;
        char ch = snd[i];
        for (char j = '0'; j <= '9' && !ok; j++)
        if (ch == '?' || ch == j)
        {
            snd[i] = j;
            ll nres = min_diff(fst, snd);
            ok |= (res == nres);
        }
        assert(ok);
    }

    printf("Case #%d: %s %s\n", test, fst.c_str(), snd.c_str());
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE

    //ios_base::sync_with_stdio(false);
    //cin.tie(0);

    int t;
    cin >> t;

    string n;
    int test = 1;
    while (cin >> n)
        solve(n, test), test++;
}
