#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-out-large.txt", "w", stdout);

	int t;
	cin >> t;

	for (int p = 0; p < t; p++) {
		int n;
		cin >> n;

		set<int> S;

		int k = n;
		int j = 0;

		while (k) {
			j++;
			k /= 10;
		}

		long long up = pow(10, j + 1);

		int flag = 0;
		long long i = 1;

		cout << "Case #" << p + 1 << ": ";
		while (1) {
			long long x = i * n;
			long long y = x;

			while (x) {
				S.insert(x % 10);
				x = x / 10;
			}
			if (S.size() == 10) {
				cout << y << endl;
				flag = 1;

				break;
			}
			i++;

			if (i == up) {
				break;
			}
		}
		if (flag == 0) {
			cout << "INSOMNIA" << endl;
		}
	}

	return 0;
}
