#include <iostream>

using namespace std;

typedef long long ll;

void solve() {
	unsigned int a, b, k;
	unsigned int i, j;
	ll res = 0;
	
	cin >> a >> b >> k;
	for (i = 0; i < a; i++) {
		for (j = 0; j < b; j++) {
			unsigned int test = i & j;
			if (test < k) {
				res++;
			}
		}
	}
	cout << res;
}

int main() {
	int cases;
	int i;
	
	cin >> cases;
	for (i = 1; i <= cases; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}