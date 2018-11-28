#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll sol[1000010];
void pre(){

	for(int i = 1; i < 1000001; ++i){
		//cout<<i<<endl;
		bool vis[10]; memset(vis, 0, sizeof vis);
		ll x;
		for(ll k = 1;true; ++k){
			bool f = false;
			x = (ll) i * k;
			ll p = x;
			while(p > 0){
				vis[p%10] = 1; p /= 10;
			}		
			for(int i = 0; i < 10; ++i) if(!vis[i]) f = true;
			if(!f) break;
		}
		sol[i] = x;
	}
}
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	pre();	
	ll t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int n; cin>>n;
			
		cout<<"Case #"<<(i+1)<<": "; 
		if(n == 0) cout<<"INSOMNIA\n";
		else cout<<sol[n]<<"\n";	
	}
	return 0;
}
