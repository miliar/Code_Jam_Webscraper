#include <bits/stdc++.h>

using namespace std;

void insertdigits(unsigned long long n, set<int> &digits)
{
	while (n) {
		int digit = n % 10;
		n /= 10;
		digits.insert(digit);
	}
}

void solve()
{
	long long number;
	cin >> number;

	if (number == 0) {
		cout << "INSOMNIA";
		return;
	}

	set<int> digits;
	for (unsigned long long i = 1; ; i++) {
		long long n = i * number;
		insertdigits(n, digits);
		if (digits.size() == 10) {
			cout << n;
			return;
		}
	}	
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}
