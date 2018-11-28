#include <bits/stdc++.h>
#include <ttmath/ttmath.h>
#define endl '\n'

using namespace std;

//typedef unsigned long long ll;
typedef ttmath::UInt<2> ll;
typedef ttmath::Big<1,2> lf;

list<ll> primes;

ll isNotPrime(ll nbr) {
	ll root = nbr;
	root.Sqrt();
	//for(ll& i : primes) {
	for(ll i = 2; i <= root; i++) {
		if(nbr%i == 0) return i;
		if(i > 4000000) break;
	}
	return 0;
}

void genPrimesList(int n) {
	ll Max = 9;
	for(int i = 0; i < n; i++) {
		Max *= 9;
	}
	Max.Sqrt();

	/*lf MaxF = Max;
	lf ln;
	ln.Ln(Max);

	lf reserveF = MaxF/ln;

	primes.reserve(reserveF.ToInt());*/

	for(ll i = 2; i <= Max; i++) {
		if(isNotPrime(i) == 0) {
			primes.push_back(i);
		}
		if(i % 1000000 == 0)
			cerr << i << "/" << Max << endl;
	}
}

string llToString(ll nbr) {
	string str = "";
	while(nbr != 0) {
		str = ((nbr%2 == 1) ? "1" : "0") + str;
		nbr /= 2;
	}
	return str;
}

ll genNbr(ll nbr, int base) {
	//if(base == 2) return nbr;
	cerr << "Calculating " << nbr << " in base " << base << "... ";

	ll ret = 0;
	ll mult = 1;
	while (nbr != 0) {
		ret += (nbr%2)*mult;

		mult *= base;
		nbr = nbr / 2;
	}
	cerr << ret << endl;
	return ret;
}

vector<ll> divisors;
bool isNotPrimeForAll(ll nbr) {
	divisors.clear();
	for(int i = 2; i <= 10; i++) {
		cerr << "Testing with base " << i << endl;
		ll ret = isNotPrime(genNbr(nbr,i));
		if(ret > 0) {
			cerr << "Not prime in base " << i << endl;
			divisors.push_back(ret);
		}
		else {
			cerr << "Prime in base " << i << endl;
			return false;
		}
	}
	return true;
}

int main() {
	ios::sync_with_stdio(false);

	int nTests;
	cin >> nTests;
	for(int test = 1; test <= nTests; test++) {
		cout << "Case #" << test << ": " << endl;
		int n,j;
		cin >> n >> j;

		int nGen = 0;
		ll nbr = 1;
		for(int i = 1; i < n; i++) nbr *= 2;
		const ll MAX = nbr*2;
		nbr++;
		cerr << "SZ " << sizeof(nbr) << endl;

		/*cerr << "Generating primes list" << endl;
		genPrimesList(n);*/

		while(nGen < j) {
			cerr << llToString(nbr) << endl;
			if(isNotPrimeForAll(nbr)) {
				cout << llToString(nbr);

				for(ll div : divisors) {
					cout << ' ' << div;
				}

				cout << endl;
				nGen++;
				cerr << llToString(nbr) << " VALID! (" << nGen << ')' << endl;
			}
			if(nGen < j) {
				cerr << "nbr=" << nbr << " max=" << MAX << " nbr+2=";
				nbr += 2;
				cerr << nbr << endl;
				if(nbr >= MAX) {
					cerr << "PASSED MAX" << endl;
					return 0;
				}
			}
		}
	}

	return 0;
}
