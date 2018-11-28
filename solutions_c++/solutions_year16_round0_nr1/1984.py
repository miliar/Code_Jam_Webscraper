#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;

ll getAns(ll n) {
	if (n == 0) return -1;
	bool seen[10];

	ll i = 1LL;
	memset(seen, 0, sizeof(seen));
	while (true) {
		ll n2 = n*i;
		while (n2 > 0LL) {
			seen[n2%10LL] = true;
			n2 = n2/10LL;
		}
		bool allSeen = true;
		for (ll j = 0LL; j < 10LL; j++) {
			if (!seen[j]) {
				allSeen = false;
				break;
			}
		}
		if (allSeen) {
			return n*i;
		}
		i++;
	}
}

void checkAll() {
	ll largestIter = 0;
	ll largestNum = 0;
	for (ll i = 1LL; i <= 1000000LL; i++) {
		ll ans = getAns(i);
		ll iter = ans / i;
		if (iter > largestIter) {
			largestIter = iter;
			largestNum = i;
		}
		if (i % 10000 == 0) {
			cerr << "checked " << i << ": " <<
				largestIter << " x " << largestNum << endl;
		}
	}
}

int main() {
	//checkAll();
	//return 1;

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int nt; cin >> nt;
	for (int ct = 1; ct <= nt; ct++) {
		ll n; cin >> n;

		ll ans = getAns(n);

		cout << "Case #" << ct << ": ";
		if (ans < 0) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << ans << endl;
		}
	}
}
