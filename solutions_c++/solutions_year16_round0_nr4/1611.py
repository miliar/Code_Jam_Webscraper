#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main() {
	freopen("inDs.txt", "r", stdin);
	freopen("outDs.txt", "w", stdout);
	ll t;
	cin>>t;
	for(int cases = 1; cases <= t; cases++) {
		ll k, c, s;
		cin>>k>>c>>s;
		cout<<"Case #"<<cases<<": ";
		for(int i=1;i<=k;i++) {
			cout<<i<<" ";
		}
		cout<<"\n";
	}
	return 0;
}