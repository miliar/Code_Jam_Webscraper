#include <cstdio>
#include <set>
using namespace std;
typedef long long ll;
ll go(ll n) {
    set<int> s;
    for ( int i = 1 ; i < 5000 ; i++ ) {
        char buf[128];
        sprintf(buf,"%lld",i*n);
        for ( int j = 0 ; buf[j] ; j++ ) 
            s.insert(buf[j]-'0');
        if ( (int)s.size() == 10 ) return i*n;
    }
    return -1;
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _tc = 1 ; _tc <= tc ; _tc++ ) {
        printf("Case #%d: ",_tc);
        ll n;
        scanf("%lld",&n);
        ll ans = go(n);
        if ( ~ans ) printf("%lld\n",ans);
        else printf("INSOMNIA\n");
    }
    return 0;
}
