#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef long long ll;

ll getval(ll c, ll b){
	ll k=1;
	ll v=0;
	while (c){
		v+=k*(c%2);
		c/=2;
		k*=b;
	}
	return v;
}

int isprime(ll x){
	for (ll t=2;t*t<=x;t++){
		if (x%t==0) return t;
	}
	return 1;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	int vv=0;
	cout<<"Case #1:"<<endl;
	for (ll i=(1<<15)+1ll;vv<50;i+=2){
		int f=0;
		vector<ll> d;
		for (ll b=2;b<=10;b++){
			ll asd=isprime(getval(i, b));
			if (asd==1) {
				f=1;
				break;
			}
			else d.push_back(asd);
		}
		if (!f){
			vv++;
			for (ll j=15;j>=0;j--){
				if ((i&(1<<j))==0) cout<<0;
				else cout<<1;
			}
			cout<<" ";
			for (ll dd:d){
				cout<<dd<<" ";
			}
			cout<<endl;
		}
	}
}