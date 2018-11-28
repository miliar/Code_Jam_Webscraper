#include <iostream>
#include <stdio.h>
#include <algorithm>
#include<string>
using namespace std;

int main() {
	int t, s, i, j, b[1001] = { 0 }, sum[1001], c = 0, diff;
	cin >> t;
	string a;
	for (i = 1; i <= t; i++)
	{
		c = 0;
		diff = 0;
		cin >> s;
		cin >> a;
		for (j = 0; j <= s; j++)
		{
			b[j] = (int)a[j] - 48;
		}

		sum[0] = b[0];
		for (j = 1; j <= s; j++)
		{
			sum[j] = sum[j - 1] + b[j];

		}
		for (j = 1; j <= s; j++)
		{
			diff = sum[j - 1] + c - j;
			if (diff<0)
			{
				c -= diff;
			}

		}
		printf("Case #%d: %d\n", i, c);
	}

	return 0;
}