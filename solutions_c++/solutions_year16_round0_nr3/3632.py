#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define MOD 1000000007LL

vector<int> v;

ll base_conv(int x, ll b){
	ll res = 0, d = 1LL;
	while (x){
		if (x & 1) res = res + d;
		d = d * b;
		x >>= 1;
	}
	return res;
}

int factor(ll n){
	if (n % 2 == 0) return 2;
	for (ll i = 3; i * i < n; i+=2){
		if (n % i == 0)
			return (int)i;
	}
	return -1;
}
int main(){
	int t;
	cin >> t;
	const int BIT_WIDTH = 15;
	const int K = 50;
	for (int i = (1 << BIT_WIDTH) + 1; i <= (1 << (BIT_WIDTH + 1)); i+=2)
		v.pb(i);

	vector<vector<ll> > res;
	int idx = 0;
	while (res.size() < K){
		vector<ll> ff;
		ff.pb(base_conv(v[idx], 10));
		bool somePrime = false;

		for (int i = 2; i <= 10; i++){
			ll n = base_conv(v[idx], i);
			int f = factor(n);
			if (f != -1)
				ff.pb(f);
			else{
				somePrime = true;
				// cout<<"skip "<<base_conv(v[idx], 10)<<" " << n << " " << i <<endl;
				break;
			}
		}
		if (somePrime == false)
			res.pb(ff);
		++idx;
	}
	cout << "Case #1: \n";
	for (int i = 0; i < res.size(); i++){
		for (ll x : res[i])
			cout << x << " ";
		cout << endl;
	}
	return 0;
}