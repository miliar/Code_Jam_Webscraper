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

using ll = long long;
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


string build(const string &s, int k)
{
    string s2(s.size(), 'G');
    string res = s;
    
    forin(i, 2, k){
        string v = res;
        res.clear();
        for ( char ch : v ){
            if ( ch == 'L' ) res += s;
            else res += s2;
        }
    }
    
    return res;
}

void solveFor(int Case, int k, int c, int s)
{
    printf ( "Case #%d:", Case);
    forin(i, 1, s) printf ( " %d", i);
    puts("");
}

void solve()
{
    int n = ni();
    
    forin(i, 1, n){
        int t = ni();
        int k = ni();
        int c = ni();
        solveFor(i, t, k, c);
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