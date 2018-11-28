#include <bits/stdc++.h>
using namespace std;

using ll = long long;
vector<ll> divisors;
vector<ll> primes;
const ll thresh = 100000000;

void init_primes_divisors(ll n) {
	primes.clear();
	divisors.clear();
	divisors.assign(n+1, 0LL);
	for(ll i=2; i<=n; ++i) {
		if(divisors[i]==0) {
			primes.push_back(i);
			for(ll j=2*i; j<=n; j+=i) {
				divisors[j] = i;
			}
		}
	}
}

vector<ll> build(int n, ll val) {
	vector<ll> res;
	for(ll base=2; base<=10; ++base) {
		ll cur = 0;
		for(int i=n-1; i>=0; --i) {
			cur = cur * base + ((val & (1LL<<i)) ? 1LL : 0LL);
		}
		if(cur<=thresh) {
			if(divisors[cur]==0) {
				res.clear();
				return res;			
			}
			res.push_back(divisors[cur]);
		} else {
			bool found = false;
			for(ll p: primes) {
				if((cur%p)==0) {
					res.push_back(p);
					found = true;
					break;
				}
			}
			if(!found) {
				res.clear();
				return res;
			}
		}
	}
	return res;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.precision(10);
	cout << fixed;
	init_primes_divisors(thresh);
	int res = 0;
	int n = 16;
	int m = n-2;
	int j = 50;
	cout << "Case #1:" << endl;
	for(ll c=0; c<(1LL<<m); ++c) {
		ll i = (1LL<<(n-1)) + (c<<1) + 1LL;
		vector<ll> d = build(n, i);
		if(!d.empty()) {
			cout << std::bitset<16>(i).to_string();
			for(ll j: d) cout << ' ' << j;
			cout << endl;
			++res;
		}
		if(res==j) break;
	}
	return 0;
}
