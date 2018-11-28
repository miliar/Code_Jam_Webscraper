#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define ABS(x) ((x)>0?(x):(-(x)))
#define sqr(x) ((x)*(x))
#define rep(i,n) for (lld i=1; i<=(n); i++)
#define For(i,s,t) for (lld i=(s); i<=(t); i++)
#define FOR(i,s,t) for (lld i=(s); i>=(t); i--)
#define foreach(it,v) for (__typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)
typedef long long lld;
typedef pair<int,int> pii;

lld n,J,we[99][99],val[99],divisor[99];

lld isprime(lld x,lld i) {
    for (lld j=2; j*j<=x; j++)
        if (x%j==0) return j;
    return 1;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    lld cas; scanf("%lld",&cas);
    For(i,2,10) {
        we[i][0]=1;
        rep(j,16) we[i][j]=we[i][j-1]*i;
    }
    rep(cs,cas) {
        printf("Case #%lld:\n",cs);
        scanf("%lld%lld",&n,&J);
        For(x,0,(1<<n)-1) if ((x&1) && ((x>>(n-1))&1))
        {
            For(i,2,10) val[i]=0;
            For(i,0,n-1) if ((x>>i)&1)
                For(j,2,10) val[j]+=we[j][i];
            bool flag=true;
            //printf("%lld\n",x);
            For(i,2,10) {
                divisor[i]=isprime(val[i],i);
                //printf("%lld %lld\n",val[i],divisor[i]);
                if (divisor[i]==1) flag=false;
            }
            //return 0;
            if (flag) {
                FOR(i,n-1,0) printf("%lld",(x>>i)&1);
                For(i,2,10) printf(" %lld",divisor[i]);
                printf("\n");
                J--;
                if (J==0) break;
            }
        }
    }
    return 0;
}
