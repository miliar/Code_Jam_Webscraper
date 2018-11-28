#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>

int ans[10], counter;
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int t;
	cin >> t;
	for (size_t i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		int n;
		counter = 0;
		memset(ans, 0, sizeof(ans));

		cin >> n;
		int nn = n;
		if (n == 0)
		{
			cout << "INSOMNIA\n";
		}
		else
		{
			while (counter < 10)
			{
				for (size_t i = 0; pow(10, i) <= nn; i++)
				{
					int temp = nn / (int)pow(10, i) % 10;
					if (!ans[temp])
					{
						ans[temp] = 1;
						counter++;
					}
				}
				nn += n;
			}
			cout << nn - n << "\n";
		}
	}
}