#include <bits/stdc++.h>

using namespace std;

int coin = 0;
int J;

long long isPrime(long long x)
{
	long long y = sqrt(x);

	for (int i = 2; i <= y; i++) {
		if (x % i == 0) {
			return i;
		}
	}

	return 1;
}

void mark(int *a, int i, int n)
{
	if (i == n - 1) {
		vector<long long> b;

		int j;
		for (j = 2; j <= 10; j++) {
			long long x = 0;

			int k = 0;
			while (k < n) {
				x = x * j + a[k];
				k++;
			}

			long long y = isPrime(x);
			if (y == 1) {
				break;
			} else {
				b.push_back(y);
			}
		}
		
		if (j == 11) {
			coin++;

			for (int k = 0; k < n; k++) {
				cout << a[k];
			}
			
			for (int k = 0; k < b.size(); k++) {
				cout << ' ' << b[k];
			}
			cout << endl;
		}
	} else {
		a[i] = 0;
		mark(a, i + 1, n);

		if (coin == J) {
			return;
		}

		a[i] = 1;
		mark(a, i + 1, n);

		
		if (coin == J) {
			return;
		}
	}
}


int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) { 
		int n;
		cin >> n >> J;

		int a[n];

		a[0] = 1;
		a[n - 1] = 1;
		
		coin = 0;

		cout << "Case #" << i + 1 << ":" << endl;

		mark(a, 1, n);
	}

	return 0;
}
