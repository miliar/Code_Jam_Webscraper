#include<cctype>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<cassert>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<unordered_map>
#include<queue>
#include<tuple>
using namespace std;
typedef long long int lnt;
typedef unsigned long long int unt;
typedef unsigned ust;
typedef double dou;
typedef pair<int,int> P;
#define FZ(i,n)       for(int i=0;i<(n);++i)
#define FB(i,n)       for(int i=(n)-1;i>=0;--i)
#define FV(i,st,ed)   for(int i{st};i<(ed);++i)
#define FC(i,n)       for(int i{n};i;--i)
#define FZU(i,n)      for(ust i{0};i!=(n);++i)
#define FVU(i,st,ed)  for(ust i{st};i<(ed);++i)
#define FCU(i,n)      for(ust i{n};i;--i)
#define SZ(x)         ((int)x.size())
#define ALL(x)        (x).begin(),(x).end()
#define likely(x)     __builtin_expect(!!(x), 1)
#define unlikely(x)   __builtin_expect(!!(x), 0)

#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RS(x) scanf("%s",x)
#define RI64(x) scanf("%I64d",&(x))
#define RII64(x,y) scanf("%I64d%I64d",&(x),&(y))

#define FIR first
#define SEC second
#define pritnf printf
constexpr ust N = 100514u;

int n,k;
dou p[256];
dou dp[256][256];
auto mdp(int c){
    int a[256],at=1;
    for(int j=0;j<n;++j)if((c>>j)%2){
        a[at++]=j;
    }
    dp[0][0]=1.0;
    FV(i,1,k+1){
        dp[i][0] = dp[i-1][0]*(1.0-p[a[i]]);
        FVU(j,1,i){
            dp[i][j] = dp[i-1][j]*(1.0-p[a[i]])+dp[i-1][j-1]*p[a[i]];
        }
        dp[i][i] = dp[i-1][i-1]*p[a[i]];
    }
    return dp[k][k/2];
}
void sol(int uuu){
    RII(n,k);
    FZU(i,n){
        dou pp;
        scanf("%lf",p+i);
    }
    dou ans = 0;
    FZ(i,1<<n)if(__builtin_popcount(i)==k){
        ans = max(ans,mdp(i));
    }
    printf("Case #%d: %.10f\n",uuu,ans);
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bs.txt","w",stdout);
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++)sol(ti);
	}
	return 0;
}

