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

 
ld dp[210][210];
ld p[210];

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

int  main()
{
    ios_base::sync_with_stdio(false);  cin.tie(0); cout.tie(0);
   //  freopen("input.txt", "r", stdin);
 //    freopen("output.txt", "w", stdout);


    int test;
    cin >> test;
    int tl = 0;
    while (test-- > 0)
    {
        tl++;
        int n, k;
        cin >> n >> k; 
        for (int i(0); i < n; i++)
            cin >> p[i];
        int m = 1 << n;
        ld ans = 0;
        for (int i(1); i < m; i++)
        {
            if (check(i) != k) continue;
            vector<ld> a;
            for (int j(0); j < n; j++)
            {
                int x = 1 << j;
                if ((x & i) != 0)
                {
                    a.pb(p[j]);
                }
            } 
            for (int i(0); i <= k; i++)
                for (int j(0); j <= k; j++)
                    dp[i][j] = 0;
            dp[0][0] = 1;
            for (int i(0); i < k; i++)
                for (int j(0); j < k; j++)
                {
                    ld q = 1 - a[i];
                    dp[i + 1][j] += dp[i][j] * q;
                    dp[i + 1][j + 1] += dp[i][j] * a[i];
                }

            ld s = dp[k][k / 2];
            if (s > ans) ans = s;
        }
        cout.precision(8);
        cout << "Case #" << tl << ": " << fixed << ans << "\n";
       
    }

}