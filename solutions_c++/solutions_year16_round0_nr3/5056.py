#include <iostream>
#include <cmath>
#include <vector>
#include <sstream>
#include <string>
#include <bitset>

#define ll unsigned long long

using namespace std;


const ll bitlen = 1000000;
bitset<bitlen> nonprimes;

bitset<bitlen> getNonPrimes() {
	bitset<bitlen> nonprimes;
	ll M = (ll)sqrt(bitlen);
	nonprimes[0] = nonprimes[1] = 1;
	for (ll i = 2; i < M; i++) {
		if (!nonprimes[i]) {
			for (ll j = i*i; j < bitlen; j += i) {
				nonprimes[j] = 1;
			}
		}
	}
	return nonprimes;
}

bool isPrime(ll n) {
	if (n < bitlen)
		return !nonprimes[n];
	ll M = (ll)sqrt(n);
	for (ll i = 2; i <= M; i++) {
		if (n%i == 0)
			return false;
	}
	return true;
}

int main() {
	ll T, N, J;
	cin >> T;
	while (T--) {
		cin >> N >> J;		
		ll start = (ll)pow(2, (N-1)) + 1LL;
		ll limit = (ll)pow(2, N);
		ll num = 0, ca = 0;
		nonprimes = getNonPrimes();

		cout << "Case #" << ++ca << ":" << endl;
		for (ll i = start; i < limit; i+=2) {
			bool fail = true;
			vector<ll> bases;
			if (!isPrime(i)) {
				bases.push_back(i);
				fail = false;
				for (ll k = 3; k <= 10; k++) {
					ll result = 0;
					for (ll j = 0; j < N; j++)
						if ( (i & (1 << j)) > 0) {
							result += (ll)pow(k , j);
						}
					if (isPrime(result)) {
						fail = true;
						break;
					}
					bases.push_back(result);
				}
			}
			if (!fail) {
				string result = "";
				for (ll j = 0; j < N; j++) {
					if ( (i & (1 << j)) > 0)
						result = "1" + result;
					else result = "0" + result;
				}				 
				cout << result;
				
				for (ll k = 0; k < bases.size(); k++) {
					ll b = bases[k];
					ll m = (ll)sqrt(b);
					for (ll j = 2; j <= m; j++)
						if (b%j == 0) {
							cout << " " << j;
							break;
						}
				}

				cout << endl;
				num++;
				if (num == J)
					break;
			}
		}
	}
}

