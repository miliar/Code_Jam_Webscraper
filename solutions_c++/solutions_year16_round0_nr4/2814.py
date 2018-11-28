#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
typedef long long ll;
ll fastPower(ll base , ll power){
	if ( power==0 )
	  return 1;
	else if(power %2 == 0 )
	  return fastPower(base*base,power/2);
	else
	 return base * fastPower(base,power-1);
}
int main(){	
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int xx=1;xx<=T;xx++){
		ll K,C,S;
		cin>>K>>C>>S;
		cout<<"Case #"<<xx<<": ";
		for(int i=1;i<=K;i++){
			cout<<i<<" ";
		}
		cout<<endl;
	}
	return 0;
}