#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef long long ll;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		ll k,c,s;
		cin>>k>>c>>s;
		ll kk=1;
		for (ll j=1;j<c;j++){
			kk*=k;
		}
		for (ll i=0;i<s;i++){
			cout<<kk*i+1ll<<" ";
		}
		cout<<endl;
	}
}