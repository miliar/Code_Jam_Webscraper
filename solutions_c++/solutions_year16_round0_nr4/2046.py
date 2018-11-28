#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>

using namespace std;

typedef long long ll;

ll p(ll a, int p) {
	ll r = 1;
	for (int i = 0; i < p; i++)
		r = r * a;
	return r;
}

int main(){
	
	int t;
	cin >> t;;
		
	for (int caso = 1; caso <= t; caso++) {
		ll k, c, s;
		cin >> k >> c >>s;
		if ((k / c + (k % c != 0)) > s)
			cout <<  "Case #" << caso << ": IMPOSSIBLE";
		else {
			ll j = c - 1;
			ll r = 0;
			cout <<  "Case #" << caso << ":";
			for (ll i = 0; i < k; i++) {
				r += i * p(k, j);
				if (j == 0 || (j > 0 && (i == k - 1))) {
					cout << " " << r + 1;
					j = c - 1;
					r = 0;
				} 
				else
					j--;
			}
		}
		cout << endl;
	}
	
	return 0;
}
