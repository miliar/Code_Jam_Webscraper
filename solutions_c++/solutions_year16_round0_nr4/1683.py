#include <iostream>
using namespace std;
typedef long long ll;

ll power(int n, int k) {
	ll ans=1ll;
	while (k--)
	  ans*=n;
	return ans;
}

int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("q4.out","w",stdout);
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		int k,c,s;
		cin>>k>>c>>s;
		ll inc=power(k,c-1);
		ll p=1ll;
		cout<<"Case #"<<T<<":";
		while (s--) {
			cout<<" "<<p;
			p+=inc;
		}
		cout<<endl;
	}
}
