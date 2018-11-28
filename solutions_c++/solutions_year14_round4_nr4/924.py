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

const int N = 1000;

set<string> Set[10];

int n, m;
string s[10];
int to[10];
int ans = 0, cnt = 0;

int calc(){
    for(int i = 0; i < n; i++) Set[i].clear();
    for(int i = 0; i < m; i++){
        string temp = "";
        for(int j = 0; j < s[i].size(); j++){
            temp += s[i][j];
            Set[to[i]].insert(temp);
        }
    }
    int res = 0;
    for(int i = 0; i < n; i++){
        res += Set[i].size() + 1;
    }
    for(int i = 0; i < n; i++){
        if(Set[i].size() == 0){
            res = -inf;
        }
    }
    return res;
}

inline void go(int x){
    if(x == m){
        int res = calc();
        if(ans < res){
            ans = res;
            cnt = 1;
        }else if(ans == res){
            ++cnt;
        }
        return;
    }
    for(int i = 0; i < n; i++){
        to[x] = i;
        go(x + 1);
    }
}

int solve(){
    m = read();
    n = read();
    for(int i = 0; i < m; i++){
        cin >> s[i];
    }
    ans = 0;
    go(0);
    printf("%d %d\n",ans,cnt);
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
        solve();
    }

    return 0;
}

