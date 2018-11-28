#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

bool mark[10] = { 0 };

bool solve(int n) {
	while (n > 0) {
		mark[n % 10] = true;
		n /= 10;
	}

	for (int i = 0; i < 10; ++i) {
		if (!mark[i])
			return false;
	}

	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	unsigned long long T, N;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> N;
		for (int j = 0; j < 10; ++j)
			mark[j] = false;

		if (N == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		int k = 1;
		while (!solve(k*N))
			++k;

		cout << "Case #" << i << ": " << k*N << endl;
	}

	return 0;
}
