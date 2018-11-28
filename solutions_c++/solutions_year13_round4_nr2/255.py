#include <iostream>
using namespace std;
typedef long long ll;
bool I(ll n, ll k, ll p) {
	if (n<=p) return 1;
	if (k==0) return 1;
	if (k==n-1) return 0;
	return I(n/2, (k+1)/2, p);
}
bool V(ll n, ll k, ll p) {
	if (k==0) return 1;
	if (p<=n/2) return 0;
	return V(n/2, (k-1)/2, p-n/2);
}
template<class F>
ll bs(ll n, ll p, F f) {
	n = 1<<n;
	ll low=0, hi=n;
	while(hi-low>1) {
		ll mid = (low+hi)/2;
		if (f(n,mid,p)) low=mid;
		else hi=mid;
	}
	return low;
}
ll guar(ll n, ll p) {
	return bs(n,p,V);
}
ll could(ll n, ll p) {
	return bs(n,p,I);
}
int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		ll n,p;
		cin>>n>>p;
		cout<<"Case #"<<a<<": "<<guar(n,p)<<' '<<could(n,p)<<'\n';
	}
}
