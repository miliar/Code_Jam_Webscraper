// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;
typedef long long LL;
int n;
LL p;
LL solve1() {
    if ( p==(1LL<<n) ) return (1LL<<n)-1;
    LL ret=0,now=0,len=2,num=1LL<<(n-1);
    while ( now+num<p ) {
        ret+=len;
        now+=num;
        len*=2;
        num/=2;
    }
    ret=min(ret,(1LL<<n)-1);
    return ret;
}
LL solve2() {
    if ( p==(1LL<<n) ) return (1LL<<n)-1;
    LL ret=0,now=0,len=1LL<<(n-1),num=1;
    while ( now+num<p ) {
        ret+=len;
        now+=num;
        len/=2;
        num*=2;
    }
    ret=min(ret,(1LL<<n)-1);
    return ret;
}
void solve() {
    scanf("%d%lld",&n,&p);
    LL a1=solve1();
    LL a2=solve2();
    printf("%lld %lld\n",a1,a2);
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

