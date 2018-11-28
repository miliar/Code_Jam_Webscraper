#include <iostream>

int main() {
	using namespace std;
	int t, n, slp[10] = { 0, }, j = 2;
	unsigned int cnt = 0, tmp = 0;

	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> n;

		if (n == 0) n = -1;

		tmp = n;

		while (cnt != 10 && n != -1) {
			
			while (1) {

				if (!(slp[tmp % 10])) {
					
					slp[tmp % 10] = 1;
					cnt++;
				}

				tmp /= 10;

				if (!tmp) break;
			}
			
			tmp = n * j;
			++j;

		}

		if (n == -1) cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else cout << "Case #" << i + 1 << ": " << n * (j - 2) << endl;

		cnt = 0;
		j = 2;

		for (int i = 0; i < 10; i++) slp[i] = 0;
	}

	return 0;
}