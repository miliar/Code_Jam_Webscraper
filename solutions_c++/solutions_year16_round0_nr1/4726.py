#include <iostream>
#include <string>
#include <algorithm>
#define ll long long
using namespace std;

void solve(ll N) {
	if (N == 0) {
		cout << "INSOMNIA\n";
		return;
	}
	bool used[10];
	int i;
	for (i = 0; i < 10; ++i) {
		used[i] = false;
	}
	ll nn, cr = 0;
	int rem = 10;
	while (rem > 0) {
		cr += N;
		nn = cr;
		while (nn > 0) {
			if (!used[nn % 10]) {
				--rem;
			}
			used[nn % 10] = true;
			nn /= 10;
		}
	}
	cout << cr << '\n';
}

int main() {
	int tc, T = 0;
	ll N;
	cin >> T;
	for (tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		cin >> N;
		solve(N);
	}
	return 0;
}