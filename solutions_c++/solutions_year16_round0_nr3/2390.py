#include<iostream>
#include<vector>
using namespace std;
#define ll long long

vector<ll> divisors;
bool isPrime(ll n) {
	for(ll i= 2; i*i <=n;i++) {
		if(n%i==0){
			divisors.push_back(i);
			return false;
		}
	}
	return true;
}

ll convertToBase(ll nbin, ll base) {
	ll ret=0, exp=1; 
	while(nbin) {
		ret += (nbin%2)*exp;
		exp*=base;
		nbin/=2;
	}
	return ret;
}

bool test(ll nbin) {
	divisors.clear();
	for (ll base = 2; base <=10; base++) {
	  ll x = convertToBase(nbin, base); 
		if (isPrime(x)) return false;
	}
	return true;
}

void printBin(ll x) {
	if (x!=0) {
		printBin(x/2);
		cout << x%2;
	}
}

int main() {
	int t, n, j;
	cin >> t >> n >> j;
	cout << "Case #1:" << endl;
	for (ll i=0;i<(1<<(n-2)); i++) {
		ll x = 1 + (i<<1) + (1<<(n-1));
		if(test(x)) {
			printBin(x);
			for (int i=0; i<divisors.size(); i++) {
				cout << " " << divisors[i];
			}
			cout << endl;
			j--;
			if(j==0)break;
		}
	}
	return 0;
}
