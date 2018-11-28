#include <iostream>
#include <vector>
#include <string>

using namespace std;

int RetDivisor(string s, int base) {
	if (base == 10)
		return 3;
	if (base % 2)
		return 2;
	if (base == 6 || base == 8) {
		long long num = 0;
		int mod = base == 6 ? 7 : 3;
		for (int i = 0; i < s.size(); i++) {
			num *= 1LL * base;
			num += s[i] - '0';
			num %= mod;
		}
		if (!num)
			return mod;
		else
			return -1;
	}


	unsigned long long num = 0;
	for (int i = 0; i < s.size(); i++) {
		num *= 1LL * base;
		num += s[i] - '0';
	}
	int limit = 100;
	if (num < limit)
		limit = num;
	for (int i = 2; i < limit - 1; i++)
		if (num % i == 0)
			return i;
	return -1;
}

int main() {
	int n = 32;
	int cnt = 500;
	freopen("output.txt", "w", stdout);
	cout << "Case #1:" << endl;
	for (int i = 0; i < (1 << (n-2)), cnt > 0; i++) {
		long long a = 1;
		for (int k = 0; k < n-2; k++) {
			a *= 2LL;
			a += ((1 << k) & i) > 0;
		}

		a *= 2LL;
		a++;
		bool valid = true;
		vector <int> divisors;

		string s = "";
		long long x = a;
		int onecount = 0;
		while (x) {
			int mod = x % 2;
			onecount += mod;
			s += (x%2) + '0';
			x /= 2;
		}
		reverse(s.begin(), s.end());

		if (onecount != 6)
			continue;

		for (int base = 2; base < 11; base++) {
			int div = RetDivisor(s, base);
			if (div == -1) {
				valid = false;
				break;
			}
			divisors.push_back(div);
 		}

		if (valid) {
			cout << s;
			for (int i = 0; i < divisors.size(); i++)
				cout << " " << divisors[i];
			cout << endl;
			cnt--;
		}
	}

	return 0;
}