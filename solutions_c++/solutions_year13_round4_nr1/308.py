//Coder: Balajiganapathi
#define TRACE
#define DEBUG

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
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros
#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define rep(i,s,n)  for(int i=s;i<=(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

const int oo = 2000000009;
const double eps = 1e-9;

#ifdef TRACE
    #define trace1(x)                cerr << #x << ": " << x << endl;
    #define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
    #define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
    #define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
    #define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
    #define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

    #define trace1(x)
    #define trace2(x, y)
    #define trace3(x, y, z)
    #define trace4(a, b, c, d)
    #define trace5(a, b, c, d, e)
    #define trace6(a, b, c, d, e, f)

#endif

const int mx = 100, mx_n = 1000000009;
const int mod = 1000002013;

int entries[mx], exits[mx];
int n, m;

int calc(ll a, ll b, ll p) {
    ll k = b - a;
    p %= mod;
    return p * ((k * (n + 1) % mod + mod - k * (k + 1) / 2 % mod) % mod) % mod;
}
int mcnt;

int main() {
    //freopen("sample.txt", "r", stdin); freopen("output.txt", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin); freopen("small0_1.txt", "w", stdout);
    freopen("A-large.in", "r", stdin); freopen("large.txt", "w", stdout);

    int _T;
    scanf("%d", &_T);
    for(int _t = 1; _t <= _T; ++_t) {
        map<int, ll> entries, exits;
        vi pts;
        ll greedy = 0, orig = 0;
        scanf("%d %d", &n, &m);
        while(m--) {
            int a, b, p;
            scanf("%d %d %d", &a, &b, &p);
            
            entries[a] += p; exits[b] += p;
            orig += calc(a, b, p);

            orig %= mod;
            
            pts.pu(a); pts.pu(b);
        }
        sort(all(pts));
        //trace1(orig);
        
        fr(i, sz(pts)) {
            
            int c = pts[i];
            for(int j = i; j >= 0; --j) {
                int p = pts[j];
                ll nw = min(entries[p], exits[c]);
                //trace3(p, c, nw);
                greedy += calc(p, c, nw);
                greedy %= mod;
                entries[p] -= nw;
                exits[c] -= nw;
            }
            
            assert(!exits[c]);
        }
        
        fr(i, sz(pts)) assert(!entries[pts[i]] && !exits[pts[i]]);
        trace2(orig, greedy);
        printf("Case #%d: %d\n", _t, (int)(((ll)orig + mod - greedy) % mod));
    }

	return 0;
}
