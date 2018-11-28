#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t;
	scanf("%d ", &t);

	for (int k = 0; k < t; k++)
	{
		int mas[105][105] = {0};
		int need[105][105] = {0};
		bool w[105][105] = {false};

		int n,m;
		scanf("%d %d ", &n, &m);

		for(int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				mas[i][j] = 100;

		vector <int> prog;
		for(int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d ", &need[i][j]);
				prog.push_back(need[i][j]);
			}
		}
		sort(prog.begin(), prog.end());
		prog.erase(unique(prog.begin(), prog.end()), prog.end());
		reverse(prog.begin(), prog.end());

		bool res = true;
		for (int ii = 0; ii < prog.size(); ii++)
		{
			int nee = prog[ii];
			bool can3 = true;
			for(int i = 0; i < n; i++)
			{
				bool  can2 = true;
				for (int j = 0; j < m; j++)
				{ 
					if (nee == need[i][j])
					{
						bool can = true;
						if (mas[i][j] == nee)
						{
							w[i][j] = true;
							continue;
						}
						for (int im = 0; im < n; im++)
						{
							if (mas[im][j] == nee)
								continue;
							if ((mas[im][j] < nee) || (w[im][j]))
							{
								can = false;
								break;
							}
						}
						if (can)
						{
							for (int im = 0; im < n; im++)
								mas[im][j] = nee;
						}
						else
						{
							can = true;
							for (int jm = 0; jm < m; jm++)
							{
								if (mas[i][jm] == nee)
									continue;
								if ((mas[i][jm] < nee) || (w[i][jm]))
								{
									can = false;
									break;
								}
							}
							if (can)
							{
								for (int jm = 0; jm < m; jm++)
									mas[i][jm] = nee;
							}
						}
						if (!can)
						{
							can2 = false;
							break;
						}
						w[i][j] = true;
						continue;
					}
				}
				if (can2 == false)
				{
					can3 = false;
					break;
				}
			}
			if (!can3)
			{
				res = false;
				break;
			}
			/*for (int i = 0; i < n; i++)
				{
					for (int j = 0; j < m ; j++)
					printf("%d ", w[i][j]);
					printf("\n");
			}
			printf("\n");*/
		}
		res = true;

		for(int i = 0; i < n; i++)
		{
			if (!res)
				break;
			for (int j = 0; j < m; j++)
			{
				if (mas[i][j] != need[i][j])
				{
					res = false;
					break;
				}
			}
		}

		if (res)
			printf("Case #%d: YES\n", k + 1);
		else
			printf("Case #%d: NO\n", k + 1);
	}
	return 0;
}