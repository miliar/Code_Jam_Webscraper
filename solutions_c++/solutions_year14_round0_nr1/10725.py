#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>
#include <cctype>
#include <stdio.h>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <stdlib.h> 
#include <algorithm>
#include <iomanip>
#include <set>
using namespace std;

int main()
{
	freopen("A-small-attempt6.in", "r", stdin);
	freopen("out.in", "w", stdout);

	int cases;
	int a, b;
	int m, n;

	cin >> cases;
	for (int l = 1; l <= cases; l++)
	{
		vector<int> x(4), y(4);
		cin >> a;
		for (int j = 1; j <= 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> m;
				if (a == j)
					x[k] = m;
			}
		}
		cin >> b;
		for (int j = 1; j <= 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				cin >> n;
				if (b == j)
					y[k] = n;
			}
		}
		int c = 0;
		for (int j = 0; j < 4; j++)
		{
			for (int i = 0; i < 4; i++)
			{
				if (x[j] == y[i])
				{
					m = x[j];
					c++;
				}
			}
		}
		if (c == 1)
			cout << "Case #" << l << ": " << m << endl;
		if (c > 1)
			cout << "Case #" << l << ": Bad magician!" << endl;
		if (c == 0)
			cout << "Case #" << l << ": Volunteer cheated!" << endl;
		x.clear(); y.clear();
	}
	return 0;
}