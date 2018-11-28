#include<bits/stdc++.h>
#define ll long long
using namespace std;
set<ll> st;

void poo(ll n) {
	while(n) {
		st.insert(n%10);
		n /= 10;
	}
	return ;
}

int main() {
	freopen("inAl.txt", "r", stdin);
	freopen("outAl.txt", "w", stdout);
	ll t;
	cin>>t;
	for(int cases = 1; cases <=t; cases++) {
		st.clear();
		ll n;
		cin>>n;
		cout<<"Case #"<<cases<<": ";
		if(!n) {
			cout<<"INSOMNIA\n";
			continue;
		}
		ll ans = 0;
		for(int i=1;;i++) {
			poo(n*i);
			if(st.size() == 10) {
				ans = n*i;
				break;
			}
		}
		cout<<ans<<"\n";
	}
	return 0;
}