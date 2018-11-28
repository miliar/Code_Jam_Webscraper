#include <bits/stdc++.h>
#include "InfInt.h"
using namespace std;

typedef InfInt ll;

ll gcd(ll a, ll b) {
	return a == 0 ? b : gcd(b % a, a);
}

ll mabs(ll n) {
	return n < 0 ? -n : n;
}

ll P[11][20];
ll F[11];
ll N;

ll factor(ll n) {
	//cerr << "n = " << n << '\n';
	ll cc = n.intSqrt().intSqrt();
	ll cs = 2;
	ll x = 2;
	ll lx = 2;
	ll fc = 1;
	while(fc == 1 && cc-- > 0) {
		//cerr << cc << " " << cs << "\n";
		for(ll cnt = 1; cnt <= cs && fc <= 1 && cc > 0; cnt++, cc--) {
			x = (x * x + 1) % n;
			fc = gcd(mabs(x - lx), n);
		}
		if(cc == 0) return 1;
		cs *= 2;
		lx = x;
	}
	return fc;
}

int main() {
	for(int b = 2; b <= 10; b++) {
		ll ml = 1;
		for(int p = 0; p <= 15; p++, ml *= b) P[b][p] = ml;
	}
	ofstream fout("out.txt");
	fout << "Case #1:\n";
	int cc = 0;
	for(ll st = 0; st < (1<<14) && cc < 50; st++) {
		//cerr << st << " " << cc << "\n";
		for(int b = 2; b <= 10; b++) {
			ll n = P[b][15] + 1;
			for(int j = 0; j < 14; j++) {
				if((st / P[2][j]) % 2 == 0) {
					n += P[b][j+1];
				}
			}
			F[b] = factor(n);
			if(b == 10) N = n;
		}
		bool ok = true;
		for(int b = 2; b <= 10; b++) {
			ok &= F[b] != 1;
		}
		if(ok) {
			cc++;
			fout << N;
			for(int b = 2; b <= 10; b++) fout << " " << F[b];
			fout << "\n";
		}
	}
}
