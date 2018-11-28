#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;
typedef long long ll;

const ll LIM = 1000000001LL;

bool is_palindrome(ll n) {
	vector<int> a;
	do {
		a.push_back(n % 10);
		n /= 10;
	} while (n);

	for (int i = 0; 2 * i < a.size(); ++i) {
		if (a[i] != a[a.size() - 1 - i]) {
			return false;
		}
	}
	return true;
}
int main() {
	ifstream in("c.out");
	vector<ll> r;
	int n;
	in >> n;
	for (int i = 0; i < n; ++i) {
		ll t;
		in >> t;
		r.push_back(t * t);
	}

	int n_tests;
	cin >> n_tests;

	for (int test = 0; test < n_tests; ++test) {
		ll a, b;
		cin >> a >> b;
		int ans = 0;
		for (int i = 0; i < r.size(); ++i) {
			if (r[i] >= a && r[i] <= b) {
				++ans;
			}
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}


	return 0;
}


