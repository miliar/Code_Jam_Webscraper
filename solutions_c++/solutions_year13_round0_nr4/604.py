#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXK = 50, MAXN = 30;

int q[MAXK];
int chest[MAXN][MAXK];
int deg[MAXN];
int needs[MAXN];
int dp[1<<20];
int k,n;

int go(int mask) {
    if(mask == (1<<n)-1) return 1; //symbolic number indicating it's possible
    if(dp[mask] != -1) return dp[mask];
    int keys[MAXN];
    memcpy(keys,q,sizeof(keys));
    for(int a=0;a<n;++a) {
        if(mask&(1<<a)) {
            keys[needs[a]]--;
            for(int b=0;b<deg[a];++b)
                keys[chest[a][b]]++;
        }
    }
    for(int a=0;a<n;++a) {
        if(mask&(1<<a) || !keys[needs[a]]) continue;
        if(go(mask^(1<<a)) != -2) return dp[mask] = a;
    }
    return dp[mask] = -2;
}    

int main() {    
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        memset(dp,-1,sizeof(dp));
        memset(q,0,sizeof(q));        
        scanf("%d%d",&k,&n);
        for(int a=0;a<k;++a) {
            int type;
            scanf("%d",&type);
            q[type]++;
        }
        for(int a=0;a<n;++a) {
            scanf("%d",&needs[a]);
            scanf("%d",&deg[a]);
            for(int b=0;b<deg[a];++b)
                scanf("%d",&chest[a][b]);
        }            
        printf("Case #%d:",t);
        if(go(0) != -2) {
            int cur = 0;
            for(int a=0;a<n;++a) {
                printf(" %d",go(cur)+1);
                cur ^= 1<<(go(cur));
            }
        }
        else printf(" IMPOSSIBLE");
        printf("\n");
    }          
    return 0;
}
