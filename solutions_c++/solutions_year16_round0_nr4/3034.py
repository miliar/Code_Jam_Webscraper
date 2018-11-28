// Fractiles.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>

using namespace std;


int main()
{
	int t, k, c, s;
	cin >> t;

	for (int x = 1; x <= t; ++x) {
		cout << "Case #" << x << ": ";
		cin >> k >> c >> s;

		if (s < (double)k / (double)c) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		long long index = 0;
		int cm = 1;
		for (int i = 0; i < k; ++i) {
			index += i * ((long long)pow(k, c - cm));
			++cm;
			if (cm > c) {
				cout << index + 1 << " ";
				index = 0;
				cm = 1;
			}
		}

		if (cm != 1) cout << index + 1 << " ";
		cout << endl;
	}

    return 0;
}

