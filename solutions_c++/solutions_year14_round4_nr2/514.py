#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector <ll> VI;
typedef vector <VI> VVI;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef pair <ll, ll> PII;
typedef set <ll> SI;
typedef map <ll, ll> MII;

int main(){
	ll T;
	cin >> T;
	for (ll t = 1; t <= T; ++t){
		ll N;
		cin >> N;
		VI v(N);
		ll tot = 0;
		for (ll i = 0; i < N; ++i) cin >> v[i];
		for (ll i = 0; i < N; ++i){
			ll posmin = 0;
			ll minim = 1e9+1;
			ll n = v.size();
			for (ll j = 0; j < n; ++j){
				if (v[j] < minim){
					minim = v[j];
					posmin = j;
				}
			}
			tot += min(posmin, n-1-posmin);
			for (ll i = posmin+1; i < n; ++i) v[i-1] = v[i];
			v.resize(n-1);
		}
		cout << "Case " << "#" << t << ": " << tot << endl;
	}
}
