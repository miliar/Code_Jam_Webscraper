
#include<cstdio>
#include<cstring>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<bitset>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<cstdlib>
#include<cmath>
#define PI 2*asin(1.0)
#define LL __int64
#define pb push_back
#define clr(a,b) memset(a,b,sizeof(a))
#define lson lr<<1,l,mid
#define rson lr<<1|1,mid+1,r
const int  MOD = 1e9 + 7;
const int N = 1e3 + 15;
const int INF = (1 << 31) - 10;
const int letter = 130;
using namespace std;
int dis[N], n;
int main() {
    freopen("B.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    int tc, cas = 0;
    scanf("%d", &tc);
    while(tc--) {
        clr(dis, 0);
        scanf("%d", &n);
        int a;
        for(int i = 0; i < n; i++) {
            scanf("%d", &a);
            dis[a]++;
        }
        int min1 = INF;
        for(int tc = 1000; tc >= 1; tc--) {
            int ans = tc;
            int ps;
            for(int i = 1; i <= 1000; i++) {
                if(dis[i] && i > tc) {
                    ps = i / tc;
                    if(i%tc==0) ps--;
                    ans += ps*dis[i];
                }
            }
            min1 = min(min1,ans);
        }
        printf("Case #%d: %d\n", ++cas, min1);
    }
    return 0;
}
