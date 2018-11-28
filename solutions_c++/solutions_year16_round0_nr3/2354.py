#include<bits/stdc++.h>
using namespace std;

bool next(int arr[], int len) {
	for (int i = 0; i < len; i++) {
		if (i == 0) {
			arr[0] = 1;
		} else if (arr[i] == 1) {
			arr[i] = 0;
		} else {
			arr[i] = 1;
			return true;
		}
	}
	return false;
}

unsigned long long represent(int arr[], int len, int base) {
	unsigned long long total = 0;
	for (int i = 0; i < len; i++) {
		total += (arr[i] == 0 ? 0 : pow(base, i));
	}
	return total;
}

int main() {
	ios_base::sync_with_stdio(0);
	freopen("prelim-c.in", "r", stdin);
	freopen("prelim-c.res", "w", stdout);

	int t;
	cin >> t;

	vector<int> prime_array;
	prime_array.push_back(2);

	for (int i = 1; i <= t; i++) {
		int n, j;
		cin >> n >> j;

		cout << "Case #" << i << ":" << endl;

		int arr[n];
		for (int j = 0; j < n; j++) {
			(j == n - 1) ? (arr[j] = 0) : (arr[j] = 1);
		}

		while (j != 0 && next(arr, n)) {
			unsigned long long coin = represent(arr, n, 10);
			string primes = "";
			bool is_prime = false;
			for (int b = 2; b <= 10; b++) {
				unsigned long long res = represent(arr, n, b);
				int a_prime = 0;

				for (int p = 0; p < prime_array.size() && p * p <= res; p++) {
					int prime = prime_array[p];
					if (res % prime == 0) { a_prime = prime; break; }
				}

				if (a_prime == 0) {
					int prime = prime_array[prime_array.size() - 1] + 1;

					while (prime * prime <= res) {
						bool is_a_prime = true;
						for (int p = 0; p < prime_array.size() && is_a_prime; p++) {
							if (prime % prime_array[p] == 0) { is_a_prime = false; }
						}

						if (is_a_prime) {
							prime_array.push_back(prime);
							if (res % prime == 0) { a_prime = prime; break; }
						}
						prime++;
					}
				}

				if (a_prime == 0) {
					is_prime = true;
					break;
				} else {
					primes += to_string(a_prime);
					primes += " ";
				}
			}

			if (!is_prime) {
				cout << coin << " " << primes << endl;
				j--;
			}
		}
	}
}
