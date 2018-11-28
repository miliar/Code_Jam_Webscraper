#include <stdio.h>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <string.h>
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<int> vi;
#define X first
#define Y second
#define all(c)	(c).begin(), (c).end()
#define sz(x)	((int) (x).size())
#define fill(c, v)	memset((c), (v), sizeof((c)))

vi fasnos;

inline ll reverse(ll n) {
	ll x = 0;
	while(n > 0) {
		x = (x*10LL) + (n % 10);
		n /= 10;
	}
	return x;
}

inline bool is_palin(ll n) {
	return n == reverse(n);
}

void generate() {
	for(ll i=1; i <= 10000000; i++)
		if (is_palin(i) && is_palin(i*i))
			fasnos.push_back(i*i);
	sort(all(fasnos));
}

int binsearch(ll k) {
	int lo = -1, hi = sz(fasnos);
	while (lo + 1 < hi) {
		int p = (lo + hi) >> 1;
		if (fasnos[p] > k) hi = p;
		else lo = p;
	}
	return lo;
}

int main() {
	generate();
	int T;
	ll a, b;
	cin >> T;

	for(int t=1; t <= T; t++) {
		cin >> a >> b;
		cout << "Case #" << t << ": " << binsearch(b) - binsearch(a-1) << endl;;
	}
	return 0;
}