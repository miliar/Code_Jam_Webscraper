#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		int counter = 0;
		int a, b, k;
		cin >> a >> b >> k;
		for (int i = 0; i < a; ++i)
		for (int j = 0; j < b; ++j)
		{
			if ((i & j) < k)
				++counter;
		}
		cout << "Case #" << test << ": " << counter << endl;
	}
}