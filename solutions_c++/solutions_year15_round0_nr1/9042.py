// /GCJ/2015/STANDINGOVATION

#include <bits/stdc++.h>

using namespace std;

int main() {
	int n_tests = 0;
	cin >> n_tests;

	for (int tc = 1; tc <= n_tests; tc++) {
		int max_shy = 0;
		cin >> max_shy;

		string shyness;
		cin >> shyness;

		long long int n_standing = 0, n_added = 0;
		for (int i = 0; i < shyness.length(); i++) {
			if (n_standing >= i)
				n_standing += shyness[i] - '0';
			else {
				n_added += i - n_standing;
				n_standing = i;
				n_standing += shyness[i] - '0';
			}
		}
		cout << "Case #" << tc << ": " << n_added << endl;
	}
	return 0;
}