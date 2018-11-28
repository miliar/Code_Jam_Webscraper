#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>

using namespace std;

bool isPalindrome(int n) {

	int num = 0, temp = n;
	while (temp)
		num *= 10, num += (temp % 10), temp /= 10;

	return num == n;
}

int main() {

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t, a, b, counter;
	double temp;

	cin >> t;
	for (int i = 1; i <= t; i ++) {

		counter = 0;
		cin >> a >> b;
		for (int j = a; j <= b; j ++) {

			if (isPalindrome(j)) {
				temp = sqrt((double)j);
				if (temp == (int)temp)
					if (isPalindrome((int)temp))
						counter ++;
			}
		}

		cout << "Case #" << i << ": " << counter << endl;
	}

	return 0;
}
