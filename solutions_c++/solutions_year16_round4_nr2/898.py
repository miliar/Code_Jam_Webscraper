#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

double f[2][19];
double p[18];

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		int k, n;
		cin >> n >> k;
		for (int i = 0; i < n; ++i)
			cin >> p[i];
		vector<int> v(n, 0);
		for (int i = 0; i < k; ++i)
			v[i] = 1;
		sort(v.begin(), v.end());
		double res = 0;
		do
		{
			int ind = 0, nind = 1;
			for (int i = 0; i < 18; ++i)
				f[0][i] = 0;
			f[0][9] = 1;
			for (int i = 0; i < n; ++i)
				if (v[i] == 1)
				{
					for (int j = 0; j < 18; ++j)
						f[nind][j] = 0;
					for (int j = 1; j < 18; ++j)
					{
						f[nind][j+1] += f[ind][j] * p[i];
						f[nind][j-1] += f[ind][j] * (1 - p[i]);
					}
					ind = nind;
					nind = 1 - ind;
				}
			res = max(res, f[ind][9]);
		}
		while (next_permutation(v.begin(), v.end()));
		
		printf("Case #%d: %.6lf\n", tt, res);
	}

	return 0;
}
