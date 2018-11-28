#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<bitset>
#include<cstdlib>
#include<cmath>
#include<set>
#include<list>
#include<deque>
#include<map>
#include<queue>
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
using namespace std;
typedef long long ll;
typedef long double ld;
const ld eps = 1e-9, PI = 3.1415926535897932384626433832795;
const int mod = 1000000000 + 7;
const int INF = 0x3f3f3f3f;
// & 0x7FFFFFFF
const int seed = 131;
const ll INF64 = ll(1e18);
const int maxn = 100;
int T,kase = 0;
bool vis[15];
ll n;

int main() {
//    ios::sync_with_stdio(false);
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt0.txt", "w", stdout);
    scanf("%d",&T);
    while(T--) {
        scanf("%lld",&n);
        ll ans = 0, cnt = 0;
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n",++kase);
            continue;
        }
        ll m = n;
        memset(vis, false, sizeof(vis));
        while(true) {
            ll cur = n;
            while(cur) {
                ll res = cur % 10;
                if(vis[res]) ;
                else {
                    vis[res] = true;
                    ++cnt;
                }
                cur /= 10;
            }
            if(cnt == 10) {
                ans = n;
                break;
            }
            n += m;
        }
        printf("Case #%d: %lld\n",++kase, ans);
    }
    return 0;
}





