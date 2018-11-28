#include <algorithm>
#include <iostream>
#include <cstring>
#include <complex>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#include <set>

#define all(x) (x).begin(), (x).end()
#define type(x) __typeof((x).begin())
#define foreach(it,x) for(__typeof(x.begin()) it = x.begin() ; it!=x.end() ; it++ )

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

const int inf = 1e9 + 143;
const long long longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

int solve(){
    int n = read(), x = read();
    vector<int> cnt(705, 0);
    for(int i = 0; i < n; i++){
        cnt[read()]++;
    }
    int res = n;
    for(int i = x; i >= 0; i--){
        for(int j = x - i; j >= 0; j--){
            if(i != j){
                int t = min(cnt[i], cnt[j]);
                cnt[i] -= t;
                cnt[j] -= t;
                res -= t;
            }else{
                res -= cnt[i] / 2;
                cnt[i] %= 2;
            }
        }
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
    for(int it = 1; it <= tc; it++){
        printf("Case #%d: ",it);
        printf("%d\n",solve());
    }

    return 0;
}

