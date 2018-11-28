#include <bits/stdc++.h>
using namespace std;
set<int>s;
#define ll long long
void dig(ll n){
	while(n>0){
		s.insert(n%10);
		n/=10;
	}
}
int main(){
     ll t,n,x=1;
     cin>>t;
      for(int i=1;i<=t;i++){s.clear();x=1;
      	cin>>n;
      	if(n==0)cout<<"Case #"<<i<<": INSOMNIA\n";
      	else {
      		while(s.size()<10){
      			dig(x*n);
      			x++;
      		}
      		ll ans=(x-1)*n;
      		cout<<"Case #"<<i<<": "<<ans<<"\n";
      	}
      }

	return 0;
}