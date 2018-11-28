// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
#define N 37
typedef long long LL;
LL b,x[N];
LL get( int p, LL m ) {
    LL need=0;
    for ( int i=0; i<=p; i++ ) need+=m-x[i];
    for ( int i=p+1; i<N; i++ ) if ( x[i]<=m ) need+=m+1-x[i];
    return need;
}
void solve() {
    int n;
    scanf("%lld%d",&b,&n);
    for ( int i=0; i<n; i++ ) scanf("%lld",x+i);
    for ( int i=n; i<N; i++ ) x[i]=0;
    sort(x,x+N);
    double ans=0;
    for ( int i=0; i<N; i++ ) {
        if ( get(i,x[i])>b ) continue;
        LL l=x[i],r=1e14;
        while ( l!=r ) {
            LL m=(l+r+1)/2;
            if ( get(i,m)<=b ) l=m;
            else r=m-1;
        }
        double cost=get(i,l);
        double back=0;
        for ( int j=0; j<=i; j++ ) back+=36.0*(l-x[j])/(i+1);
        //printf("%d: l = %lld, cost = %g, back = %g\n",i,l,cost,back);
        ans=max(ans,back-cost);
    }
    printf("%.12f\n",ans);
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
