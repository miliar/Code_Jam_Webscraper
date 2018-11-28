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

const int N = 1010;

int a[N], b[N];

int f[N];

void init(){
    for(int i = 0; i < N; i++) f[i] = 0;
}

int get(int x){
    int s = 0;
    while(x > 0){
        s += f[x];
        x -= x & -x;
    }
    return s;
}

void put(int x){
    while(x < N){
        f[x]++;
        x += x & -x;
    }
}

int calc(int n){
    init();
    int s = 0;
    for(int i = n - 1; i >= 0; i--){
        s += get(b[i]);
        put(b[i]);
    }
    return s;
}

int solve(){
    int n = read();
    vector<int> vals;
    for(int i = 1; i <= n; i++){
        a[i] = read();
        vals.push_back(a[i]);
    }
    sort(vals.begin(), vals.end());
    for(int i = 1; i <= n; i++){
        a[i] = lower_bound(all(vals), a[i]) - vals.begin() + 1;
        eprintf("%d ",a[i]);
    }
    eprintf("\n");
    int mx = 1;
    for(int i = 2; i <= n; i++){
        if(a[i] > a[mx]){
            mx = i;
        }
    }
    int ans = inf;
    for(int mask = 0; mask < (1 << n); mask++){
        if(!(mask & (1 << (mx - 1))))
            continue;
        int sz = 0;
        int cur = 0;
        for(int i = 1; i <= n; i++){
            if(mask & (1 << (i - 1))){
                b[sz++] = a[i];
                cur += abs(i - sz);
            }
        }
        cur += calc(sz);
        sz = 0;
        for(int i = 1; i <= n; i++){
            if(!(mask & (1 << (i - 1)))){
                b[sz++] = a[i];
            }
        }
        reverse(b, b + sz);
        cur += calc(sz);
        umin(ans, cur);
    }
    return ans;
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

