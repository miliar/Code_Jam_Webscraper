/*
Problem #524 Prime Ring Problem - UVA
http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=465
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	
	ll a, ans;
	bool found = false;

	ll t, i, j;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		cin >> i;
		ans = 0;
		found = false;
		for (j = 1; j < 1000000; j++)
		{
			a = i * j;
			while (a)
			{
				ans |= 1 << (a % 10);
				a /= 10;
			}

			if (ans == (1 << 10) - 1)
			{
				found = true;
				break;
			}
		}

		if (!found)
			printf("Case #%d: INSOMNIA\n", z);
		else
			printf("Case #%d: %lld\n", z, i * j);
	}
	return 0;
}
