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

set<int> getNums(int num)
{
    set<int> ans;
    while ( num > 9 ){
        ans.insert(num % 10);
        num /= 10;
    }
    ans.insert(num);
    return ans;
}

void solveCase(int Case, int num)
{
    set<int> s;
    int val = num;
    
    while ( true ){
        auto v = getNums(val);
        s.insert(v.begin(), v.end());
        if ( val + num == val ) break;
        if ( s.size() == 10 ) break;
        val += num;
    }
    
    if ( s.size() < 10 )
        printf ( "Case #%d: INSOMNIA\n", Case);
    else printf ( "Case #%d: %d\n", Case, val);
}

void solve()
{
    int n = ni();
    
    forin(i, 1, n)
    {
        int k = ni();
        
        solveCase(i, k);
    }
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#endif
    
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    srand((int)clock());
    
    solve();
    
    return 0;
}