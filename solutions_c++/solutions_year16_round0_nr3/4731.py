#include <iostream>
#include <cmath>
#include <random>
#include <map>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
#define ll long long

ll trans(ll num, int p)
{
	ll ans = 0;
	for (int i = 0; num > 0; i++) {
		ans = ans + (num % 10) * (ll)pow(p, i);
		num = num / 10;
	}
	return ans;
}

ll prime(ll num)
{
	ll up = (int)sqrt(num) + 1;
	ll ok = 0;
	for (ll i = 2; i < up; i++) {
		if (num % i == 0) {
			ok = i;
			break;
		}
	}
	return ok;
}

int check(ll num)
{
	int ok = 0;
	for (int i = 2; i <= 10; i++) {
		if (prime(trans(num, i)) == 0) break;
		if (i == 10) ok = 1;
	}
	if (ok) return 1;
	else return 0;
}

int main(void)
{
	srand(15);
	int t;
	int n, j;
	cin >> t >> n >> j;

	ll c;

	int count = 0;
	map<ll, int> w;

	cout << "Case #1:" << endl;

	
	while(1) {
		c = 1000000000000001;
		// c = 100001;
		rep(i, n - 2) c += (rand() % 2) * (ll)pow(10, i + 1);
		if (w[c]) continue;
		else w[c] = 1;
		if (check(c)) {
			count++;
			cout << c;
			for (int k = 2; k <= 10; k++) cout << " " << prime(trans(c, k));
			cout << endl;
			// for (int k = 2; k < 10; k++) cout << trans(c, k) << " ";
			// cout << endl;
		}
		if (count == j) break;
	}
	
	return 0;
}

