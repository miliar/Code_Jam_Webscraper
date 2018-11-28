#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;
#define see(x) cout<<#x<<" "<<x<<endl

const ll maxn = 10000010LL;

vector<ll> pot;

bool isPa(ll n) {
	ll t = 0, p = n;
	for(; p != 0; ) {
		t *= 10LL;
		t += p%(10LL);
		p /= 10LL;
		// if(t < 0)
		// 	see(n);
	}
	return n == t;
}

int main() {

	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);

	// isPa(123456789012345);

	for(ll i = 0; i < maxn; ++i) {
		if(isPa(i) && isPa(i*i)) {
			pot.push_back(i);
			// see(i);
			// see(i*i);
		}
	}

	ll t, T;
	cin>>T;
	for(t = 1; t <= T; ++t) {
		ll a, b;
		cin>>a>>b;
		ll res = 0;
		for(ll i = 0, l = pot.size(); i < l && pot[i]*pot[i] <= b; ++i)
			if(pot[i]*pot[i] >= a) {
				++res;

			}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}

}