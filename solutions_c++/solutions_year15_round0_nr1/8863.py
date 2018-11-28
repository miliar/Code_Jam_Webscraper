#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
	ll t;
	cin>>t;
	for(int i=1;i<=t;i++){
		ll n;
		cin>>n;
		ll tsum=0,sum=0,req =0;
		string s;
		cin>>s;
		tsum = s[0]-'0';
		for(int j=1;j<=n;j++){
			if( (tsum) < j && (s[j]-'0') > 0 ){
				sum += (j-tsum);
				tsum = j;
			}
			tsum += (s[j] - '0');
		} 
		cout<<"Case #"<<i<<": ";
		cout<<(sum)<<endl;
	}
	return 0;
}