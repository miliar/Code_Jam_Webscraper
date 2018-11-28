//Coder: Balajiganapathi
#ifndef ONLINE_JUDGE
#   define DEBUG
//#   define TRACE
#else
//#   define NDEBUG
#endif

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;
typedef vector<pi> vpi;

// Basic macros
#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fo(i,n)     re(i,0,n)
#define rev(i,n,s)  for(int i=(n)-1;i>=s;--i)
#define repv(i,n,s) for(int i=(n);i>=s;--i)
#define fov(i,n)    rev(i,n,0)
#define pu          push_back
#define mp          make_pair
#define si(x)       (int)(x.size())

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif

const int oo = 1000000009;
const double eps = 1e-6;
const int mod = 1000000007;
const int mx = 10005;

int n, p;
ll e[mx], f[mx], sub1[mx], sub2[mx], ans[mx];
int get(ll from) {
    int j = lower_bound(e, e + p, from) - e;
    assert(e[j] == from);
    return j;
}
int main() {
    //freopen("sample.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("small0.txt", "w", stdout);

    //freopen("D-large.in", "r", stdin);
    //freopen("large.txt", "w", stdout);
    
    int kases;
    scanf("%d", &kases);
    for(int kase = 1; kase <= kases; ++kase) {
        printf("Case #%d:", kase);
        scanf("%d", &p);
        fo(i, p) scanf("%lld", e + i);
        fo(i, p) scanf("%lld", f + i);
        int n = 0;
        ll cnt = 0;
        fo(i, p) cnt += f[i];
        for(; (1ll << n) < cnt; ++n);
        trace2(n, p);

        ini(sub1, 0);
        --f[get(0)]; ++sub1[get(0)];

        fo(idx, n) {
            trace1(idx);
            fo(i, p) trace3(i, e[i], f[i]);
            int nxt = -1;
            fo(i, p) if(f[i]) {
                nxt = i;
                break;
            }
            assert(nxt != -1);
            ans[idx] = e[nxt];

            ini(sub2, 0);
            fo(i, p) if(sub1[i]) {
                ll from = e[i] + ans[idx];
                int j = get(from);
                trace4(idx, ans[idx], from, j);
                sub2[j] += sub1[i];
            }
            fo(i, p) {
                f[i] -= sub2[i];
                sub1[i] += sub2[i];
            }
        }

        sort(ans, ans + n);
        fo(i, n) printf(" %lld", ans[i]);
        printf("\n");
    }
    
	return 0;
}
