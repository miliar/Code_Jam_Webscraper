#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <math.h>
#include <iomanip>
#include <bitset>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long LL;
typedef pair<int,int> pii;
#define CLR(x,y) memset(x,y,sizeof(x));
#define PB push_back
#define MP make_pair
#define FOR(i,x,y) for(int i = (x) ; i < (y) ; ++i)
#define ROF(i,x,y) for(int i = (y)-1 ; i >= (x); --i)
#define FORG(i,x,g) for(int i = g.head[(x)] ; ~i ; i = g.next[i])
#define INF 0x3f3f3f3f

int T,cases;


int c,k,s;

void solve() {
    if(c==1 && s<k) {
        printf("IMPOSSIBLE\n");
        return ;
    }
    if(c>1 && s*2<k) {
        printf("IMPOSSIBLE\n");
        return ;
    }
    if(c>1) {
        LL tail = k;
        LL cell = 1;
        for(int i = 1 ; i < c ; ++i)cell*=k;
        for(int i = 1 ; i <= tail ; ++i) {
            printf("%I64d ", (LL)(i-1)*cell+k-i+1);
            --tail;
        }
        printf("\n");
    } else {
        for(int i = 1 ; i <= k ; ++i) printf("%d ",i);
        printf("\n");
    }
}

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small.out","w",stdout);
    scanf("%d",&T);
    for(cases = 1 ; cases <= T ; ++cases) {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ", cases);
        solve();
    }
}

