#include <iostream>

#define ll long long


using namespace std;

void solve(ll n) {
	if (n == 0) {
		cout << "INSOMNIA" << endl;
		return ;
	}
	bool  used[10];
	for (int i = 0; i < 10; i++) {
		used[i] = false; 
	}

	ll m = 1;

	while (true) {

		ll value = m * n;

		while (value > 0) {
			used[value % 10] = true;
			value /= 10;
		}



		bool is_end = true;
		for(int i = 0; i < 10;i++) {
			if (!used[i]) {
				is_end = false;
				break;
			}
		}
		if (is_end) {
			break;
		}
		m++;
	}

	cout << m * n << endl;
}




int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		cout << "Case #" << i + 1 << ": ";
		solve(N);
	}
	return 0;
}