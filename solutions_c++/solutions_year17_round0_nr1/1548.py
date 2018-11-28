#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define pb push_back
#define ff first
#define ss second
using namespace std;

string str;
ll n,k,tc;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		bool flag = 1;
		ll ans = 0;
		cin>>str>>k;
		n = str.length();
		for(ll i=0;i<=n-k;i++){
			if(str[i] == '-'){
				ans++;
				for(ll j=i;j<i+k;j++){
					if(str[j] == '+')
						str[j] = '-';
					else
						str[j] = '+';
				}
			}
		}
		for(ll i=0;i<n;i++){
			if(str[i] == '-')
				flag = 0;
		}
		cout<<"Case #"<<t<<": ";
		if(flag)
			cout<<ans<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
	
	return 0;
}

