#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <random>
#include <string>


using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	
	cin >> t;

	for (int k = 1; k <= t; ++k)
	{
		int x, y, z;

		cin >> x >> y >> z;

		int res = 0;

		for (int i = 0; i < x; ++i)
			for (int j = 0; j < y; ++j)
				if ((i & j) < z)
					++res;

		printf("Case #%i: %i\n", k, res);
	}

	return 0;
}
