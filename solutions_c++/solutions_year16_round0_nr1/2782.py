#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	bool digits[10];
	for (int g = 1; g <= t; ++g) {
		long long n;
		cin >> n;
		for (int i = 0; i < 10; ++i)
			digits[i] = false;
		if (n == 0) {
			cout << "Case #" << g << ": INSOMNIA" << '\n';
			continue;
		}
		bool isEnd = true;
		int k = 2, q = n;
		while (true) {
			long long temp = q;
			while (temp > 0) {
				digits[temp % 10] = true;
				temp /= 10;
			}
			isEnd = true;
			for (int i = 0; i < 10; ++i) {
				if (!digits[i]) {
					isEnd = false;
					break;
				}
			}
			if (!isEnd)
				q = n * k++;
			else
				break;
		}
		cout << "Case #" << g << ": " << q << '\n';
	}
	return 0;
}