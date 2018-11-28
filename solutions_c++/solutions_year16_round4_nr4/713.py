#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <ctime>
#include <iostream>
#include <cmath>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cassert>


const long double PI(acosl(-1.0));

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define eps 1e-7
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)


using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector < ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;
 

int check(int x)
{
    int k = 0;
    while (x > 0)
    {
        k += x % 2;
        x = x / 2;
    }
    return k;
}

string s[5];
string c[5];

int f[5];
int p[5];
int n;
int f1[5]; 

bool dfs1(int v)
{
    if (v == n)
    { 
        return true;
    }
    bool fl = false;
    for (int i(0); i < n; i++)
    {
        if (f1[i] != 0 || c[p[v]][i] == '0') continue;
        f1[i] = 1;
        fl = true;
        bool fl1 = dfs1(v + 1);
        f1[i] = 0;
        if (!fl1) return false;
    }
    return fl;
} 

bool make()
{
    for (int i(1); i <= n; i++)
        p[f[i]] = i - 1;
    return dfs1(0);
}

bool dfs(int v)
{
    if (v == n)
    { 
        bool fl = make();
        return fl;
    }
    for (int i(1); i <= n; i++)
    {
        if (f[i] != -1) continue;
        f[i] = v;
        bool fl = dfs(v + 1);
        f[i] = -1;
        if (!fl) return false;
    }
    return true;
}

bool checker()
{
    for (int i(1); i <= n; i++)
        f[i] = -1;
    return dfs(0);
}

int  main()
{
    ios_base::sync_with_stdio(false);  cin.tie(0); cout.tie(0);
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);


    int test;
    cin >> test;
    int tl = 0;
    while (test-- > 0)
    {
        tl++;
        cin >> n; 
        int ans = n * n;
        int m = 1 << ans;
        for (int i(0); i < n; i++)
        {
            cin >> s[i];
            c[i].clear();
            c[i].resize(n);
        }
        for (int j(0); j < m; j++)
        {
            int k = check(j);
            if (k >= ans) continue;
            bool fl = false;
            for (int i(0); i < n*n; i++)
            {
                int t = i / n;
                int x = i - t * n;
                int y = 1 << i;
                if ( (y & j) != 0 && s[t][x] == '1')
                {
                    fl = true; break;
                }
                 if ((y & j) != 0) c[t][x] = '1';
                else c[t][x] = s[t][x];
            }
            if (fl) continue; 
            if (checker())
                ans = k;
        }
        cout << "Case #" << tl << ": " << ans << "\n"; 
       
    }


}