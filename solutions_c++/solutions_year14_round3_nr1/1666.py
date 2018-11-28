#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

ll mcd(ll a, ll b) {
	if (b == 0)
		return a;
	else
		return mcd(b, a % b);
}

int numBit(int x) {
	int res = 0;
	while (x > 1) {
		x >>= 1;
		res++;
	}
	return res+1;
}

int solve() {
	ll a, b;
	scanf("%Ld/%Ld", &a, &b);
	
	ll m = mcd(a, b);
	a /= m;
	b /= m;
	
	if (b != (1 << (numBit(b)-1)))
		return -1;
	
	int res = 0;
	
	while (a < b) {
		res++;
		b /= 2;		
	}
	
	return res;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int res = solve();
		if (res == -1)
			cout << "Case #" << t << ": impossible" << endl;
		else
			cout << "Case #" << t << ": " << res << endl;
	}
}
