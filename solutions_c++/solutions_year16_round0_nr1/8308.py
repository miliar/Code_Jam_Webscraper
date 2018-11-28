# include <iostream>

using namespace std;
typedef long long ll;

void solve() {
	ll n;
	cin >> n;
	bool was[10];
	for(int i = 0; i < 10; ++i) {
		was[i] = 0;
	}
	for(int it = 1; it <= 100000000; ++it) {
		ll x = 1ll * n * it;
		do{
			was[x % 10] = 1;
			x /= 10;
		}while(x > 0);
		bool ok = 1;
		for(int i = 0; i < 10; ++i) {
			ok &= was[i];
		}
		if(ok) {
			cout << 1ll * n * it << '\n';
			return;
		}
	}
	cout << "INSOMNIA\n";
}

int main () {
	int t;
	cin >> t;
	for(int it = 1; it <= t; ++it) {
		cout << "Case #" << it << ": ";
		solve();
	}

	return 0;
}