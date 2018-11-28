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
		int n;
		cin >> n;
		vector<string> strs(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> strs[i];
		}
		vector<string> strs1(n);
		for (int i = 0; i < n; ++i)
		{
			strs1[i].push_back(strs[i][0]);
			for (int j = 1; j < strs[i].length(); ++j)
			{
				if (strs[i][j] != strs1[i].back())
				{
					strs1[i].push_back(strs[i][j]);
				}
			}
		}

		bool flag = true;

		for (int i = 1; i < n && flag; ++i)
		{
			if (strs1[i] != strs1[i - 1])
			{
				flag = false;
			}
		}

		if (!flag)
		{
			printf("Case #%i: Fegla Won\n", k);
		}
		else
		{
			vector<vector<int>> a(n);
			for (int i = 0; i < n; ++i)
			{
				a[i].push_back(1);
				for (int j = 1; j < strs[i].length(); ++j)
				{
					if (strs[i][j] != strs[i][j-1])
					{
						a[i].push_back(1);
					}
					else
					{
						++a[i].back();
					}
				}
			}

			vector<int> b(a[0].size());

			for (int i = 0; i < b.size(); ++i)
			{
				for (int j = 0; j < n; ++j)
				{
					b[i] += a[j][i];
				}
				b[i] = (b[i] + n/ 2) / n;
			}
			int res = 0;
			for (int i = 0; i < b.size(); ++i)
			{
				for (int j = 0; j < n; ++j)
				{
					res += abs(b[i] - a[j][i]);
				}
			}
			printf("Case #%i: %i\n", k, res);

		}
	}

	return 0;
}
