#include <iostream>
#include <algorithm>

using namespace std;

typedef long long int ll;

void test_case(int t) {
	ll N;
	cin >> N;
	cout << "Case #" << t << ": ";
	if (N == 0) {
		cout << "INSOMNIA\n";
		return;
	}
	
	bool cifre[10];
	for (int i=0; i<10; i++) cifre[i] = false;
	int viste = 0;
	ll n = 0;
	while (viste < 10) {
		n = n+N;
		ll x = n;
		while (x != 0) {
			if (!cifre[x%10]) {
				cifre[x%10] = true;
				viste++;
			}
			x = x/10;
		}
	}
	cout << n << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t=1; t <= T; t++)
		test_case(t);
	
	return 0;
}
