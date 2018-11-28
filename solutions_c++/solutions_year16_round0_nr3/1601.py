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
#include <unordered_map>
#include <unordered_set>
#include <bitset>

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

using ll = __int128; //long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

template<class T> inline bool Min(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> inline bool Max(T &a, T b) { return a < b ? (a = b, true) : false; }

inline void pi(int a) { printf("%d ", a); }
inline void pl(ll a) { printf("%lld ", a); }
inline void pd(double a) { printf("%.12lf ", a); }

inline int ni(){ int a; scanf("%d", &a); return a; }
inline ll nl(){ll a; scanf("%lld", &a); return a; }
inline double nd(){double a; scanf("%lf", &a); return a; }
//////////////////////////////////////////////////////////////////////////////

vector<int> generate_(int len)
{
    vector<int> ans;
    ans.push_back(1);
    forn(i, len-2) ans.push_back(rand()%2);
    ans.push_back(1);
    return ans;
}

inline vector<int> GetPrimeVector( int n )
{
    vector<char> ans(n+1, true);
    ans[1] = false;
    for ( int i = 2; i*i <= n; i++ )
        if ( ans[i] )
            for ( int j = i * i; j <= n; j+= i )
                ans[j] = false;
    vector<int> res;
    for ( int i = 2; i <= n; i++ )
        if ( ans[i] ) res.push_back(i);
    return res;
}

vector<int> primes;

int is_good(ll num)
{
    for ( int v : primes ){
        if ( v >= num ) break;
        if ( num % v == 0){
            return v;
        }
    }
    
    return 0;
}

ll go(vector<int> &v, int base)
{
    ll res = 0;
    ll p = 1;
    
    for ( int i = v.size() - 1; i >= 0; i-- ){
        res += p * v[i];
        p *= base;
    }
    
    return res;
}

void solve()
{
    primes = GetPrimeVector(1e5);
    
    //vector<pair<vector<int>, vector<int> > > ans;
    
    set<pair<vector<int>, vector<int> > > ans;
    while ( ans.size() < 500 )
    {
        auto cur = generate_(32);
        
        vector<int> v;
        forin(i, 2, 10){
            ll number = go(cur, i);
            if ( int k = is_good(number) )
                v.push_back(k);
        }
        
        if ( v.size() == 9 ){
            ans.insert(mp(cur, v));
        }
    }
    
    printf ( "Case #1:\n" );
    
    for ( auto &cur : ans )
    {
        forn(i, cur.fi.size()) printf("%d", cur.fi[i]);
        forn(i, 9) printf ( " %d", cur.se[i]);
        
        puts("");
    }
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    srand((int)clock());
    
    solve();
    
    return 0;
}