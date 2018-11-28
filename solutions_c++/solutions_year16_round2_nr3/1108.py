/*input
3
3
HYDROCARBON COMBUSTION
QUAIL BEHAVIOR
QUAIL COMBUSTION
3
CODE JAM
SPACE JAM
PEARL JAM
2
INTERGALACTIC PLANETARY
PLANETARY INTERGALACTIC
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long 
#define pb push_back
typedef pair<ll,ll> P;
#define mp make_pair
#define fi first
#define sc second
#define INF 100000000
int main()
{
	ll T;
	 cin >> T;

	for(ll k=1;k<=T;k++)
	{
	
		string x[16],y[16];
		ll a[16],b[16];
		ll n; cin >> n;
		map<string,ll>M,N;
		for(ll i=0;i<n;i++){
			cin >> x[i] >> y[i];
			M[x[i]] = 0;
			N[y[i]] = 0;
		}
		ll nx = 1;
		for(map<string,ll>::iterator it=M.begin();it!=M.end();it++){
			it->sc = nx++;
		}
		nx = 1;
		for(map<string,ll>::iterator it=N.begin();it!=N.end();it++){
			it->sc = nx++;
		}
		for(ll i=0;i<n;i++){
			
			a[i] = M[x[i]];
			b[i] = N[y[i]];
		}
			cout<<"Case #"<<k<<": ";
		ll dp[(1<<16)+5]={}; fill(dp,dp+(1<<n),-100000);
		dp[0] = 0;
		for(ll i=0;i<(1<<n);i++){
			ll L=0,R=0;
			for(ll j=0;j<n;j++){
				if(((i>>j)&1)){
					L |= (1<<a[j]);
					R |= (1<<b[j]);
				}
			}
			for(ll j=0;j<n;j++){
				if(!((i>>j)&1)){
					ll ad = ( (L|(1<<a[j]))==L && (R|(1<<b[j]))==R );
					dp[i+(1<<j)] = max(dp[i+(1<<j)],dp[i]+ad);
				}
			}
		}
		cout << dp[(1<<n)-1] << endl;
	}
}