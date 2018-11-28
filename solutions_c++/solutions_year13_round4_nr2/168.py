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

int n;
ll p;

ll high(ll l, ll r)
{
    if (r == 0) return l;
    if (l & 1)
    {
        r--, l++;
    }
    l /= 2;
    r--;
    r /= 2;
    return high(l, r);
} 

ll low(ll l, ll r)
{
    if (l == 0) return 0ll;
    ll start = (l + r + 1) / 2;
    if (r & 1)
    {
        r++, l--;
    }
    r /= 2;
    l--;
    l /= 2;
    return start + low(l, r);
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> n >> p;
    ll lf = 0, rg = (1ll << n) - 1;
    while (rg - lf > 1)
    {
        ll x = (lf + rg) / 2;
        if (low(x, (1ll << n) - x - 1) < p)
        {
            lf = x;
        }
        else
        {
            rg = x - 1;
        }
    }
    for (ll x = rg; x >= lf; x--)
    {
        if (low(x, (1ll << n) - x - 1) < p)
        {
            cout << x << " ";
            break;
        }
    }

    lf = 0, rg = (1ll << n) - 1;
    while (rg - lf > 1)
    {
        ll x = (lf + rg) / 2;
        if (high(x, (1ll << n) - x - 1) < p)
        {
            lf = x;
        }
        else
        {
            rg = x - 1;
        }
    }
    for (ll x = rg; x >= lf; x--)
    {
        if (high(x, (1ll << n) - x - 1) < p)
        {
            cout << x << endl;
            break;
        }
    }

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
