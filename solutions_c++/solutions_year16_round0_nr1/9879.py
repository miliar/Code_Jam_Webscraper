#include <cstdio>
using namespace std;
typedef long long ll;
const int target = (1<<10)-1;
int main(){
    int t; scanf("%d",&t);
    for( int cs = 1 ; cs <= t ; ++cs) {
        ll n; scanf("%lld",&n);
        if ( n == 0 ){
            printf("Case #%d: INSOMNIA\n",cs);
            continue;
        }
        ll orgin = n;
        ll cur = 0;
        while(1){
            ll k = n;
            while( k ){
                cur |= 1<<(k%10);
                k /= 10;
                if( k == 0 ) break;
            }
            if( cur == target ) break;
            n += orgin;
        }
        printf("Case #%d: %lld\n", cs,n);
    }
    return 0;
}