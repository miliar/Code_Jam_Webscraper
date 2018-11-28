// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>

using namespace std;


int main()
{
	int t, n;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		vector<bool> digits;
		digits.resize(10);

		int multiple = 0;
		int digCount = 0;

		int j = 1;
		while (digCount < 10) {
			multiple = j*n;
			while (multiple > 0) {
				if (!digits[multiple % 10]) {
					digCount++;
					digits[multiple % 10] = true;
				}
				multiple /= 10;
			}
			++j;
		}

		cout << "Case #" << i << ": " << (j-1)*n << endl;
	}

    return 0;
}

