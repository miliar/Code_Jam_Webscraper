#include <bits/stdc++.h>
#include <fstream>
#define X first
#define Y second
#define pb push_back
#define popb pop_back
#define mp make_pair
#define cin fin
#define cout fout
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> point;

ifstream fin("B-large.in");
ofstream fout("B-large.out");


void print(ll n, ll level) {
	cout << "Case #" << level << ": " << n << endl; 
	return;
}

ll T, ans, D, P[1200];

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for(ll level = 1; level <= T; level++) {
		cin >> D;
		ans = 1000 * 1000;
		for(ll i = 0; i < D; ++i)
			cin >> P[i];
		for(ll i = 1; i < 1010; ++i) {
			ll tmp = 0;
			for(ll j = 0; j < D; ++j) {
				if(P[j] > i)
					tmp += ((P[j] + (i - 1)) / i - 1);
			}
			if(ans > tmp + i)
				ans = tmp + i;
		} 		
		print(ans, level);
	}
	return 0;
}