/*==================================================*\
 | Author: ziki
 | Created Time: 
 | File Name: 
 | Description: 
\*==================================================*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
 
using namespace std;
using namespace rel_ops;
 
typedef long long int64;
typedef long long ll;
typedef unsigned long long uint64;
typedef unsigned long long ull;
const double pi=acos(-1.0);
const double eps=1e-11;
const int inf=0x7FFFFFFF;
template<class T> inline bool checkmin(T &a,T b){return b<a?a=b,1:0;}
template<class T> inline bool checkmax(T &a,T b){return b>a?a=b,1:0;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define mem(a,b) memset(a, b, sizeof(a))
#define clr(a) memset(a, 0, sizeof(a))
#define rep(i,n) for(int i=0; i<int(n); i++)
#define repit(i,v) for(typeof(v.begin()) i=v.begin(); i!=v.end(); i++)
#define iter(v) typeof(v.begin())
#define ff first
#define ss second
#define sz(x) int(x.size())
#ifdef LOCAL
#define dbg(args...) printf(args); //##__VA_ARGS__
#define dout cout
#define out(x) (cout<<#x<<": "<<x<<endl)
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}
#else
#define dbg(...)
#define dout if(true);else cout
#define out(...)
#define show(...)
#endif

int dir[4][2] = {0, 1, -1, 0, 0, -1, 1, 0,};
int mp[5555][5555];
int n, m;
int clk;
int dfs(int u, int v, int d) {
    if (mp[u][v] != 0) return false;
    if (v+1==m) {
        mp[u][v] = clk;
        return 1;
    }
    for (int k = d+1+4; k>= d-1+4; k--) {
        int tx = u + dir[k%4][0], ty = v + dir[k%4][1];
        if (tx < 0 || tx >= n || ty < 0 || ty >= m) continue;
        mp[u][v] = -2;
        if (dfs(tx, ty, k%4)) {
            mp[u][v] = clk;
            return 1;
        }
    }
    return false;
}

int main() {
    int T;
    scanf("%d", &T);
    rep(cas, T) {
        int k;
        scanf("%d%d%d", &n, &m, &k);
        clr(mp);
        rep(t, k) {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int i = x1; i <= x2; i++)
                for (int j = y1; j <= y2; j++)
                    mp[i][j] = -1;
        }
        int ans = 0;
        clk = 0;
        for (int i = 0; i < n; i++) {
            clk++;
            if (dfs(i, 0, 0)) ans++;
        //show(mp, n, m);
        }
        printf("Case #%d: %d\n", cas+1, ans);
    }
    return 0;
}
