#include <iostream>
#include <algorithm>
#include <assert.h>
#include <cstring>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <time.h>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
#define mp make_pair
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define for1(i, n) for(int i = 1; i < (int)(n); ++i)
#define forin(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

template<class T> inline bool Min(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> inline bool Max(T &a, T b) { return a < b ? (a = b, true) : false; }

inline int    ni() { int    a; scanf("%d",   &a); return a; } // next_int();
inline ll     nl() { ll     a; scanf("%lld", &a); return a; } // next_long();
inline double nd() { double a; scanf("%lf",  &a); return a; } // next_double();

inline void pi(int    a) { printf ( "%d ",      a); }
inline void pl(ll     a) { printf ( "%lld ",    a); }
inline void pd(double a) { printf ( "%.12lf ",  a); }
///////////////////////////////////////////////////////////////////////////////

//double dp[202][202];

double solve(int n, int k, vector<double> &a)
{
    double ans = 0;
    
    for ( int mask = 0; mask < (1 << n); mask++ ){
        int cnt = 0;
        
        for ( int i = 0; i < n; i++ )
            if ( mask & (1 << i) )
                cnt++;
     
        if ( cnt == k )
        {
            int s = mask;
            
            double sum = 0;
            
            while ( s > 0 )
            {
                cnt = 0;
                double prob = 1.0;
                
                for ( int i = 0; i < n; i++ ){
                    if ( mask & (1 << i)){
                        if ( !(s & (1 << i)) )
                            prob *= 1 - a[i], cnt++;
                        else
                            prob *= a[i];
                    }
                }
                
                if ( cnt == k / 2 )
                    sum += prob;
                
                s = (s - 1) & mask;
            }
            
            Max(ans, sum);
        }
    }
    
    return ans;
    
    /*//forn(o, 2) forn(i, 202) forn(j, 102) dp[o][i][j] = 0;
    
   // dp[0][0][0] = dp[1][0][0] = 1.0;
    
    vector<vector<double>> dp(n+1, vector<double>(k+1));
    dp[0][0] = 1;
    
    int cur = 1;
    int pred = 0;
    
    for ( int o = 0; o < n; o++ )
    {
        double yes = a[o];
        double no = 1.0 - a[o];
        
        for ( int i = min(o + 1, k); i; i-- )
        {
            Max(dp[i][0], dp[i-1][0] * no);
            
            for ( int j = 1; j <= k; j++ )
                Max(dp[i][j], dp[i-1][j-1] * yes + dp[i-1][j] * no);
        }
        
        swap(cur, pred);
    }
    
    return dp[k][k/2];
     */
}

void solve()
{
    int t = ni();
    forin(i, 1, t)
    {
        int n = ni();
        int k = ni();
        vector<double> a(n);
        forn(j, n) a[j] = nd();
        
        printf ( "Case #%d: %.10f\n", i, solve(n, k, a));
    }
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    solve();
    
    return 0;
}