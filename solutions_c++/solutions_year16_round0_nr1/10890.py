/**************************************************
****I have been back!
****Because I have a dream!
****That one day I must be that a strong man !
****--------Written by Apllo.
***************************************************/
///#pragma GCC optimize ("O2") ///G++用，
///#pragma comment(linker, "/STACK:36777216")///C++用
///#pragma comment(linker, "/STACK:102400000,102400000")///C++用，防止栈溢出
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <algorithm>
#include <bitset>
#include <deque>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;


#define debug       cout << "***********************" << endl
#define Bug(s)      cout << "s = " << s << endl
#define mem(a,b)    memset(a, b, sizeof(a))
#define lson        l, mid, rt<<1
#define rson        mid + 1, r, rt<<1|1
#define For(i, x, n)  for(int i = (x) ; i < (n) ; ++i)
#define Forr(i, x, n) for(int i = (x) ; i <= (n) ; ++i)
#define Rep(i, x, n)  for(int i = (x) ; i > (n) ; --i)
#define Repp(i, x, n) for(int i = (x) ; i >= (n) ; --i)
#define highint( n )  ceil( n )
#define lowint( n )   floor( n )
#define SERU(x)       floor((double) x + 0.5 )
#define lowbit(x)     (x & (-x))

#define all(x)      (x).begin(), (x).end()
#define SZ(x)       (int)(x).size()
#define FA(i, a, x) for (__typeof((x).begin()) i=(a); i!=(x).end(); ++i)
#define RA(i, x)    FA(i, (x).begin(), x)
#define FDA(i, a, x)  for (__typeof((x).rbegin()) i=(x).rbegin(); i!=(a); ++i)
#define RDA(i, x)   FDA(i, (x).rend(), x)
#define P(v, x)     (v.find(x) != v.end())
#define Pos(v, x)   (find(all(v), x) != v.end())
#define UN(a)       sort(all(a)), a.erase(unique(all(a)), a.end())
#define REV(a)      reverse(all(a))
#define mp(a, b)    make_pair(a, b)
#define p(a, b)     pair<int, int>(a, b)
#define sf1i(x)     scanf("%d", &x)
#define sf1l(x)     scanf("%I64d", &x)
#define sf2i(x, y)  scanf("%d%d", &x, &y)
#define sf2l(x, y)  scanf("%I64d%I64d", &x, &y)
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define ll long long
#define eps 1e-8


typedef pair<int, int> pii;
typedef vector< int > vi;
typedef vector< ll > vl;
typedef vector< vl > vvl;
typedef vector< vi > mati;
typedef vector< vl > matl;
typedef vector< double > vd;
typedef vector< string > vs;
typedef complex< double > cp;
typedef istringstream ISS;
typedef ostringstream OSS;


template<class T> inline void checkmin(T &a, T b) { if (b<a) a=b; }
template<class T> inline void checkmax(T &a, T b) { if (b>a) a=b; }
//template<class T> inline void swap(T& x , T& y){ x ^= y; y ^= x; x ^= y; }
//template<class T> inline T gcd(T a, T b) { if( a < b )swap(a, b); return b == 0 ? a : gcd(b, a % b);}
template<class T> inline T abs(T x) { return x < 0 ?  -x : x ;}
template<class T> inline T extgcd(T a, T b, T& x, T& y){
    int d = a; if(b != 0){
        d = extgcd(b, a%b, y, x);
        y -= (a / b) * x;
    }
    else {
        x = 1; y = 0;
    }
    return d;
}
template<class T> inline T mypow(T n, T k){ T res = 1; for(T i = 0; i < k; ++i)res *= n; return res;}
template<class T> inline T mod_pow(T x, T n, T mod){T res = 1; while( n ){if( n & 1)res = res * 1LL * x % mod; x = x * 1LL * x % mod; n >>= 1; } return res;}
template<class T> inline T add(int* b, int i, T x, int N){
    while(i <= N){
        *(b + i) += x;
        x += lowbit(x);
    }
}

template<class T> inline T getsum(int* b, int i){
    T res = 0;
    while(i > 0){
        res += *(b + i);
        i -= lowbit(i);
    }
    return res;
}

template<class T> inline void add_mod(T &a, int mod = -1) {
	if(mod == -1) mod = 1e9 + 7;
	while(a >= mod) a -= mod;
	while(a < 0) a += mod;
}
/********************************************************/

const int maxn = 1e5 + 10;
const ll mod  = (ll)1e9 + 7;
const int inf  = 2147483647;
const int sigma_size = 26;
const ll LLMAX = 0x7fffffffffffffffLL;
const ll LLMIN = 0x8000000000000000LL;
const int INF  = 2147483647;
const int IMIN = 0x80000000;
const ll MOD   = 1000000007LL;
const double pi = acos(-1.0);

/********************************************************/
inline int pdt(int x,int y) {  ///加速x * y % MOD
  int ret; __asm__ __volatile__ ("\tmull %%ebx\n\tdivl %%ecx\n":"=d"(ret):"a"(x),"b"(y),"c"(MOD));
  return ret;
}
#define freopenin
#define freopenout
ll gcd(ll a, ll b, ll *x, ll *y)
{
    ll tx, ty;
    ll g;

    if (b > a)
        return gcd(b, a, y, x);

    if (b == 0)
    {
        *x = 1;
        *y = 0;

        return a;
    }

    g = gcd(b, a % b, &tx, &ty);

    *x = ty;
    *y = tx - floor(a / b) * ty;

    return g;
}

int vis[10];
int main(){
        ios_base::sync_with_stdio(0);///g++输入加速
        #ifdef cc
        int __size__ = 256 << 20; // 256MB  G++
        char *__p__ = (char*)malloc(__size__) + __size__;
        __asm__("movl %0, %%esp\n" :: "r"(__p__));
        #endif // cc
        #ifdef  freopenin
            freopen("in.txt","r",stdin);
        #endif // freopenin

        #ifdef freopenout
            freopen("out1.txt","w",stdout);
        #endif // freopenout
        int T;
        scanf("%d", &T);
        for(int icase = 1; icase <= T; ++icase){
        ll n;
        scanf("%I64d", &n);
        int flag = 0, res = 0;
        memset(vis, 0, sizeof(vis));
        for(ll i = 1; i <= 10000; ++i){
            ll tmp = i * n;
            while(tmp){
                vis[(tmp%10)] = 1;
                tmp /= 10;
            }
            flag = 0;
//            cout << n * i << '\n';
            for(int j = 0; j <= 9; ++j)if(vis[j])flag ++;
            if(flag == 10){res = i; break;}
        }
        printf("Case #%d: ", icase);
        if(flag == 10)printf("%I64d\n", res * 1LL * n);
        else printf("INSOMNIA\n");
        }
        return 0;
}
