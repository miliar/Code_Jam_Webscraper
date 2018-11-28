#include<bits/stdc++.h>
 
using namespace std;
typedef long long ll;
ll dpp[1005],dpm[1005];

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	ll t,tc = 1;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		ll ans = 0,n = s.length();
		for(ll i = 0;i<1005;i++)
		dpp[i] = 0,dpm[i] = 0;
		
		if(s[0] == '+')
		dpm[0] = 1;
		else
		dpp[0] = 1;
		
		for(ll i = 1;i<n;i++){
			if(s[i] == '+'){
				dpp[i] = min(dpp[i-1],dpm[i-1] + 1);
				dpm[i] = min(dpp[i-1] + 1,dpm[i-1] + 2);
			}
			else{
				dpp[i] = min(dpm[i-1] + 1,dpp[i-1] + 2);
				dpm[i] = min(dpp[i-1] + 1,dpm[i-1]);
			}
		}
		cout<<"Case #"<<tc<<": "<<min(dpp[n-1],dpm[n-1]+1)<<endl;
		tc++;
	}
	return 0;
} 
