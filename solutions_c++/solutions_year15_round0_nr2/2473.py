#include <bits/stdc++.h>
#define ll long long
using namespace std;

int a[10007];

void solve() {
	int d; cin>>d;
	for(int i=0;i<d;i++) cin>>a[i];
	ll ans = 0x3f3f3f3f;
	for(int i=1;i<=1000;i++) {
		ll tmp = i;
		for(int j=0;j<d;j++) {
			tmp += (a[j]-1)/i;
		}
		ans = min(ans,tmp);
	}
	cout<<ans<<"\n";
}

int main() {
	int t;cin>>t;
	for(int qq=1;qq<=t;qq++) {
		cout<<"Case #"<<qq<<": ";
		solve();
	}
}
