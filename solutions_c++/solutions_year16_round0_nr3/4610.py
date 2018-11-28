#include <bits/stdc++.h>
using namespace std;

#define min(a, b) ((a) < (b) ? (a) : (b)) 
#define INF 1000000000

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ll;

ll _sieve_size;
bitset<50000010> bs;
vi primes;

void sieve(ll upperbound){
	_sieve_size = upperbound + 1;
	bs.set();
	bs[0] = bs[1] = 0;
	for (ll i = 2; i <= _sieve_size; i++)
		if (bs[i]){
			for (ll j = i * i; j <= _sieve_size; j+=i)
				bs[j] = 0;
			primes.push_back((int)i);
		}
}

ll factor(ll N) {
	ll PF_idx = 0, PF = primes[PF_idx];
	while (PF * PF <= N){
		if (N % PF == 0){
			return PF;
		}
		PF = primes[++PF_idx];
	}
	return 0;
}

int main() {
	sieve(50000000);
	int t, n, j;
	cin >> t >> n >> j;
	int cnt = 0;
	cout << "Case #1: " << endl;
	// cout << ((1ll<<(n-1))+1) << endl;
	for (ll tmp = (1ll<<(n-1))+1; tmp < (1ll<<n) && cnt < j; tmp+=2ll) {
		vi bit;
		ll num = tmp;
		if (num == 2)
			break;
		while (num > 0) {
			bit.push_back(num%2);
			num /= 2;
		}
		int yes = 1;
		vi fac;
		for (int i = 2; i <= 10; i++) {
			ll cur = 0ll;
			for (int j = bit.size()-1; j >= 0; j--)
				cur += pow(i, j) * bit[j];
			int f = factor(cur);
			if (!f) {
				yes = 0;
				break;
			}
			fac.push_back(f);
		}
		if (yes) {
			for (int i = bit.size()-1; i >= 0; i--) 
				cout << bit[i];
			for (int i = 0; i < fac.size(); i++)
				cout << " " << fac[i];
			cout << endl;
			cnt++;
		}
	}
}