#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define MMAX 1005
#define NMAX 105

string s[MMAX];
int n, m;
ll ans2 = 1;

const ll mod = 1000000007;

ll fact[NMAX];
ll c[NMAX][NMAX];

int calc(int L, int R, int p)
{
    vector<int> sz;

    int l = L;
    while (l < R && (int)s[l].size() <= p) l++;   
    if (l > L) sz.pb(l - L);

    int ans = 0;

    while (l < R)
    {
        int r = l;
        while (r < R && s[l][p] == s[r][p]) r++;
        ans += min(n, r - l) + calc(l, r, p + 1);
        sz.pb(r - l);
        l = r;
    }

    int sum = 0, mx = 0;
    forv(i, sz)
    {
        sum += sz[i];
        mx = max(mx, sz[i]);
    }
    
    if (sum >= n)
    {
        if (mx >= n)
        {
            forv(i, sz)
            {
                if (sz[i] < n)
                {
                    ans2 = (((ans2 * c[n][sz[i]]) % mod) * fact[sz[i]]) % mod;
                }
            }
        }
        else
        {
            ll a[NMAX];
            ll res = 0;
            for1(k, n)
            {
                a[k] = 1;
                forv(i, sz)
                {
                    if (sz[i] > k) a[k] = 0;
                    else
                        a[k] = (((a[k] * c[k][sz[i]]) % mod) * fact[sz[i]]) % mod;
                }
                a[k] = (a[k] * c[n][k]) % mod;
                if ((n - k) & 1) res = (res - a[k] + mod) % mod; 
                else res = (res + a[k]) % mod;
            }
            ans2 = (ans2 * res) % mod;
        }
    }
    return ans;
}

void solve(int test)
{
    printf("Case #%d: ", test);
    cerr << "Case#" << test << endl;

    scanf("%d %d\n", &m, &n);

    forn(i, m)
    {
        getline(cin, s[i]);
    } 
  
  /*
    n = 100; m = 1000;
    forn(i, m)
    {
        s[i] = "";
        forn(j, 100)
        {
            s[i] += char('A' + rand() % 26); 
        }
    }
 */
    sort(s, s + m);

    ans2 = 1;
    cout << calc(0, m, 0) + n << " ";
    cout << ans2 << endl;

}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    fact[0] = 1;
    for1(i, 100) fact[i] = (fact[i - 1] * i) % mod;

    forn(i, NMAX)
    {
        c[i][0] = c[i][i] = 1;
        for1(j, i - 1)
        {
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod;
        }
    }

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
