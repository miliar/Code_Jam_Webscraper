#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define inf 1000000000
#define eps 1e-9
#define all(a)   a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define sz size()
#define mod 1000000007
#define sl(inp) scanf("%lld",&inp)
#define sd(inp) scanf("%d",&inp)
#define rep(i, a, b) for(int i = a; i < b ; ++i)
#define maxn 1000101

ll fpow(ll base,ll power){
	ll result = 1;
    while (power > 0){
    	if (power%2 == 1){
    		result=(result*base);
    	}
    	base = (base*base);
    	power/=2;
    }
	return result;
}

int main(){
    ll t, in = 1;
    sl(t);    
    while(t--){
        string str;
        cin >> str;
        ll i;
        ll ans = 0 ;
        bool f = 0;
        for ( i = 0 ; i < str.sz ; i ++ ){
            if ( str[i] == '-'  && f == 0 ){
                if( i > 0 && str[i-1] != '-') {
                    ans ++;
                }
                else if( i == 0 ) {
                    ans ++;
                }
            }
            else if ( str[i] == '+' ){
                f = 1;
            }
            else if( str[i] == '-' && f ){
                if(i > 0 && str[i-1] != '-') {
                    ans += 2;
                }
            }
        }
        printf("Case #%lld: %lld\n", in++, ans );
    }
    return 0;
}
