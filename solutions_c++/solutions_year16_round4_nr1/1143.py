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

char win(char a, char b)
{
    if ( a > b ) swap(a, b);
    if ( a == 'R' ) return 'S';
    if ( b == 'R' ) return 'P';
    return 'R';
}

int P, R, S;

void dfs(int pos, char winner, vector<char> &xs)
{
    if ( pos + pos >= xs.size() ){
        xs[pos] = winner;
        if ( winner == 'R' ) R++;
        if ( winner == 'P' ) P++;
        if ( winner == 'S' ) S++;
        return;
    }
    
    if ( winner == 'S' )
    {
        dfs(pos+pos, 'P', xs);
        dfs(pos+pos+1, 'S', xs);
    }
    else if ( winner == 'R' )
    {
        dfs(pos+pos, 'R', xs);
        dfs(pos+pos+1, 'S', xs);
    }
    else
    {
        dfs(pos+pos, 'P', xs);
        dfs(pos+pos+1, 'R', xs);
    }
}

void minimize(string &s, int l, int r)
{
    if ( l + 1 == r ){
        return;
    }
    
    int mid = (l + r) / 2;
    
    minimize(s, l, mid);
    minimize(s, mid, r);
    
    int cnt = mid - l;
    
    for ( int i = 0; i < cnt; i++ ){
        if ( s[l + i] != s[mid + i] )
        {
            if ( s[l + i] > s[mid + i] )
            {
                for ( int j = 0; j < cnt; j++ )
                    swap(s[l++], s[mid++]);
            }
            break;
        }
    }
}

string solve(int n, int p, int r, int s)
{
    string res;
    string ans = "Z";
    
    n = 1 << n;
    vector<char> xs(n+n);
    
    res.clear();
    R = P = S = 0;
    dfs(1, 'R', xs);
    
    if ( R == r and S == s and P == p ){
        for ( int i = n; i < xs.size(); i++ )
            res.push_back(xs[i]);
        minimize(res, 0, n);
        Min(ans, res);
    }
    
    res.clear();
    R = P = S = 0;
    dfs(1, 'P', xs);
    
    if ( R == r and S == s and P == p ){
        for ( int i = n; i < xs.size(); i++ )
            res.push_back(xs[i]);
        minimize(res, 0, n);
        Min(ans, res);
    }
    
    res.clear();
    R = P = S = 0;
    dfs(1, 'S', xs);
    
    if ( R == r and S == s and P == p ){
        for ( int i = n; i < xs.size(); i++ )
            res.push_back(xs[i]);
        minimize(res, 0, n);
        Min(ans, res);
    }
    
    if ( ans == "Z" ) return "IMPOSSIBLE";
    return ans;
}

void solve()
{
    int t = ni();
    forin(i, 1, t)
    {
        int n = ni();
        int r = ni();
        int p = ni();
        int s = ni();
        
        printf ( "Case #%d: %s\n", i, solve(n, p, r, s).c_str());
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