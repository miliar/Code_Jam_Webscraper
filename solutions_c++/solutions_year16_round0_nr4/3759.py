/* My First Template  
   :P
*/
#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long int
#define pb push_back
#define mk make_pair
ll power(ll a, ll b) {
ll x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>mod) x%=mod;
        }
        y = (y*y);
        if(y>mod) y%=mod;
        b /= 2;
    }
    return x;
}
int main() 
{
	freopen("input4.in","r",stdin);
	freopen("output4.txt","w",stdout);
	ll t,k,c,s,i,j;
	ll tc = 1;
	cin>>t;
	while(t--) {
		cin>>k>>c>>s;
		vector<ll>ans;
		ll cnt = 1,x,y;
		if(k == 1) {
			ans.pb(1);
		}
		else {
			c = min(c,k);
			cnt = k;
			if(c != 1) {
				cnt += 1-c;
				for(i = x = 0,y = 1; i < c; i++) {
					y += x;
					x = (x*k)+1;
				}
				for(i = 0; i < cnt; i++) {
					ans.pb(y);
					y += x;
				}
			}
			else {
				for(i = 1; i <= k; i++) {
					ans.pb(i);
				}
			}
		}
		if(s < cnt) {
			cout<<"Case #"<<tc<<": "<<"IMPOSSIBLE"<<endl;
		}
		else {
			cout<<"Case #"<<tc<<":";
			for(i = 0; i < ans.size(); i++) {
				cout<<" "<<ans[i];
			}	
			cout<<endl;
		}
		tc++;
	}
	return 0;
}

