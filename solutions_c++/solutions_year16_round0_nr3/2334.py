#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> digits;
int n, j;

long long toTen(int base) {
	long long res = 0;
	for (int i = 0; i < digits.size(); ++i)
		res += digits[n - 1 - i] * (long long)pow(base, i);
	return res;
}

void incNum() {
	++digits[n - 2];
	int i = n - 2;
	while (i < n && digits[i] > 1) {
		digits[i] %= 2;
		++digits[--i];
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n >> j;
	digits.resize(n);
	for (int i = 0; i < digits.size(); ++i)
		digits[i] = 0;
	digits[0] = 1;
	digits[n - 1] = 1;
	cout << "Case #1:\n";
	while (j != 0) {
		vector<long long> divs;
		for (int i = 2; i <= 10; ++i) {
			long long num = toTen(i);
 			for (long long j = 2; j <= (long long)sqrt(num); ++j) {
				if (num % j == 0) {
					divs.push_back(j);
					break;
				}
			}
		}
		if (divs.size() == 9) {
			for (int i = 0; i < digits.size(); ++i)
				cout << digits[i];
			cout << ' ';
			for (int i = 0; i < divs.size(); ++i)
				cout << divs[i] << ' ';
			cout << '\n';
			--j;
		}
		incNum();
	}
	return 0;
}