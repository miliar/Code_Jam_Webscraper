// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cassert>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
#define M 1010
#define MOD 1000002013
LL sum( LL l, LL r ) { return (l+r)*(r-l+1)/2; }
int st[M],ed[M],p[M];
PII evt[2*M];
void solve() {
    int n,m;
    scanf("%d%d",&n,&m);
    for ( int i=0; i<m; i++ ) scanf("%d%d%d",st+i,ed+i,p+i);
    LL ans=0;
    for ( int i=0; i<m; i++ ) ans=(ans+sum(n-(ed[i]-st[i]-1),n)%MOD*p[i])%MOD;
    int ne=0;
    for ( int i=0; i<m; i++ ) evt[ne++]=PII(st[i],-p[i]);
    for ( int i=0; i<m; i++ ) evt[ne++]=PII(ed[i],p[i]);
    sort(evt,evt+ne);
    vector<PII> stk;
    for ( int i=0; i<ne; i++ ) {
        //printf("i = %d, (%d,%d)\n",i,evt[i].first,evt[i].second);
        PII now=evt[i];
        if ( now.second<0 ) {
            stk.push_back(PII(now.first,-now.second));
        } else {
            while ( now.second>0 ) {
                assert(!stk.empty());
                PII top=stk.back();
                stk.pop_back();
                LL cost=sum(n-(now.first-top.first-1),n)%MOD;
                LL num=min(top.second,now.second);
                ans=(ans-cost*num)%MOD;
                top.second-=num;
                now.second-=num;
                if ( top.second>0 ) stk.push_back(top);
            }
        }
    }
    if ( ans<0 ) ans+=MOD;
    printf("%lld\n",ans);
}
int main()
{
    int num_case;
    scanf("%d",&num_case);
    for ( int i=1; i<=num_case; i++ ) {
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}

