#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    ll n, x,ans;
    int t;
    scanf("%d",&t);
    for(int i = 1; i<=t; ++i){
    	scanf("%lld",&n);
    	printf("Case #%d: ",i);
    	if(!n){
    		puts("INSOMNIA");
    		continue;
    	}
    	set <ll> st;
        ans = 0;
    	while(1){
    		if(st.size() == 10) break;
    		ans += n;
    		x = ans;
    		while(x){
    			st.insert(x%10);
    			x /= 10;
    		}
    	}
    	printf("%lld\n",ans);
    }
	return 0;
}
