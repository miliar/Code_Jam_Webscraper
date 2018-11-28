#include <algorithm>
#include <iostream>
#include <cstring>
#include <complex>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <bitset>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

#define all(x) (x).begin(), (x).end()
#define type(x) __typeof((x).begin())
#define foreach(it, x) for(type(x) it = (x).begin(); it != (x).end(); it++)

#ifdef KAZAR
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

typedef long long ll;
typedef pair<int, int> ii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 1010;

int c[N];

int solve(){
    int n = read();
    for(int i = 0; i <= n; i++){
        char foo;
        scanf(" %c", &foo);
        c[i] = foo - '0';
    }
    int cur = c[0];
    int res = 0;
    for(int i = 1; i <= n; i++){
        if(cur < i){
            res += i - cur;
            cur = i;
        }
        cur += c[i];
    }
    return res;
}

int main(){
    
#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    int tc = read();
    
    for(int i = 1; i <= tc; i++){
        printf("Case #%d: %d\n", i, solve());
    }
    
    return 0;
}

