#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)1e3 + 10;
const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll INF = (ll)1e18;
const double eps = (int)1e-9;

string f[maxn], s[maxn];
char first[maxn], second[maxn];
map <string, int> was;
int a[maxn], b[maxn], wass[maxn], wasf[maxn];

int solve()
{
    int n, ans = 0;
    scanf("%d", &n);
    
    int id = 0;
    was.clear();
    for (int i = 0; i < n; ++i)
    {
        scanf("%s %s", first, second);
        f[i] = first;
        s[i] = second;
        
        if (was[f[i]])
            a[i] = was[f[i]];
        else
            a[i] = was[f[i]] = ++id;
        
        if (was[s[i]])
            b[i] = was[s[i]];
        else
            b[i] = was[s[i]] = ++id;
    }
    
    for (int mask = 0; mask < (1 << n); ++mask)
    {
        bool bad = false;
        for (int i = 0; i < n; ++i)
        {
            if (mask & (1 << i))
                wasf[a[i]] = wass[b[i]] = true;
        }
        for (int i = 0; i < n; ++i)
        {
            if (!wasf[a[i]] || !wass[b[i]])
                bad = true;
        }
        if (!bad)
            ans = max(ans, n - __builtin_popcount(mask));
        for (int i = 0; i < n; ++i)
            wasf[a[i]] = wass[b[i]] = false;
    }
    return ans;
}

int main()
{
    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; ++i)
        printf("Case #%d: %d\n", i, solve());
    return 0;
}