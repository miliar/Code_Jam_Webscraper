#include <iostream>
#include <vector>

using namespace std;

typedef vector <bool> VB;
typedef long long ll;



ll f(ll n){
	VB v = VB(10, false);
	ll cont = 10;
	ll i = 1;
	ll N = n;
	while (cont > 0){
		ll m = N;
		while (m > 0){
			ll x = m%10;
			if (!v[x]){
				v[x] = true;
				--cont;
				if (cont == 0) return N;
			}
			m/=10;
		}
		N +=n;
	}
}

int main(){
	ll T;
	cin >> T;
	for (ll i = 0; i < T; ++i){
		ll n;
		cin >> n;
		cout << "Case #" << i+1 << ": ";
		if (n == 0) cout << "INSOMNIA" << endl;
		else cout << f(n) << endl;
	}
		
}
