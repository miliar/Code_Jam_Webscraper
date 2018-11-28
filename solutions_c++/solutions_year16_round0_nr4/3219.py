#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	long long ans;
	long long t;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		long long k, s, c;
		long long ans = 0;
		cin >> k >> c >> s;
		cout << "Case #" << i + 1 << ":";
		if (s < k)
		{
			cout << "IMPOSSIBLE\n";
			continue;
		}

		long long table[105];
		table[0] = 1;
		for (size_t s = 1; s <= 100; s++)
		{
			table[s] = table[s - 1] * k;
		}
		for (size_t s = 0; s < k; s++)
		{
			ans = 0;
			for (size_t q = 1; q <= c; q++)
			{
				ans += table[q - 1] * s;
			}
			ans += 1;
			cout << " " << ans;
		}
		cout << "\n";

	}
}