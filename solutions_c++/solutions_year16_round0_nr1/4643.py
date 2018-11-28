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

pair<ll,ll> precal[10];

inline void pre(){
	ll i;
	for( i = 0 ; i < 10 ; i ++ ){
		precal[i].ff = (i*2)%10;
		if(i*2 >= 10){
			precal[i].ss = 1;
		}
		else{
			precal[i].ss = 0;
		}
	}
}

bool vis[10];

bool ch(){
	ll x;
	for ( x = 0 ; x < 10 ; x ++ ){
		if( vis[x] == 0 ){
			return 1;
		}
	}
	return 0;
}

inline void mark(ll temp){
	while ( temp > 0 ){
		vis[temp%10] = true;
		temp /= 10;
	}
}

int main(){
    ll t, in = 1;
    sl(t);
    while(t--){
    	ll n;
    	sl(n);
    	memset(vis, 0, sizeof(vis));
    	ll i = 1;
    	bool f = 0;
    	bool flag = 0;
    	while(ch()){
    		f = 1;
    		ll here = i * n;
    		mark(here);
    		i = i + 1;
    		if( i == 10000 ){
    			flag = 1;
    			goto there;
    		}
    	}
    	if( f == 1){
    		i = i - 1;
    	}
    	if(!flag) printf("Case #%lld: %lld\n", in++, i * n);
    	there:;
    	if(flag){
    		printf("Case #%lld: INSOMNIA\n", in++);
    	}
    }
    return 0;
}
