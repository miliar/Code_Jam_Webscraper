#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

vector<ll> x;
ll b;

bool can(ll c)
{
    ll s = 0;
    forv(i, x)
    {
        if (x[i] < c) s += c - x[i];
        if (s > b) return false;
    }
    return true;
}

double calc(ll c)
{
    if (c <= 0) return 0.0;
    if (!can(c)) return 0.0;

    int cnt = 0;
    ll bet = 0;
    forv(i, x) if (x[i] <= c) 
    {
        bet += c - x[i];
        cnt++;
    }

    int eq = 0;
    forv(i, x) if (x[i] == c) eq++;

    double ans = 0;

    for (int add = 0; add < cnt && bet + add <= b; add++)
    {

        double ret = 0.0;
        forn(i, cnt - add)
        {
            ret += ((c - x[i]) * 36) * 1.0 / (cnt - add);
        }

        ans = max(ans, ret - bet - add);
    }

    return ans;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    int n;
    cin >> b >> n;
    x = vector<ll>(n);
    forn(i, n) cin >> x[i];
    while (x.size() < 37) x.pb(0ll);
    sort(all(x));

    double best = 0;

    /*forv(i, x)
    {
        best = max(best, calc(x[i]));
        best = max(best, calc(x[i] - 1));
        best = max(best, calc(x[i] + 1));
    }

    ll lf = 0, rg = b;
    while (rg - lf > 2ll)
    {
        ll mid = (lf + rg) / 2;
        if (!can(mid)) rg = mid - 1; else lf = rg;    
    }

    for (ll c = lf; c <= rg; c++) best = max(best, calc(c));
    */   

    for (ll c = 1; c <= x.back() + b; c++) best = max(best, calc(c));    

    printf("%.12lf\n", best);
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
