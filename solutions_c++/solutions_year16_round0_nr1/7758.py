#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e6 + 6;
typedef long long ll;

ll n;

void solve(){
    set< int > st;
    for( int i = 1; i <= 20000; ++i ){
        ll x = i * n;
        while( x > 0 )
            st.insert( x % 10 ),
            x /= 10;
        if( st.size() == 10 ){
            return (void)( printf("%lld\n", n * (ll)i) );
        }
    }
    puts("INSOMNIA");
}

int main(){
    int T; scanf("%d", &T);
    for( int kase = 1; kase <= T; ++kase ){
        printf("Case #%d: ", kase);
        scanf("%lld", &n);
        solve();
    }
    return 0;
}
