#include <iostream>
#include <fstream>
using namespace std;

typedef long long ll;

ll getAns(ll n) {
	ll x, i = 1, remainingDigits = 10;
	bool digits[10] = {};

	while (remainingDigits > 0) {
		x = i++ * n;

		while (x > 0) {
			if (!digits[x % 10]) {
				digits[x % 10] = true;
				remainingDigits--;
			}

			x /= 10;
		}
	}

	return n * (i - 1);
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int t, n, ans;
	fin >> t;

	for (int k = 1; k <= t; k++) {
		fin >> n;

		if (n == 0)
			fout << "Case #" << k << ": " << "INSOMNIA" << endl;
		else
			fout << "Case #" << k << ": " << getAns(n) << endl;
	}

	return 0;
}