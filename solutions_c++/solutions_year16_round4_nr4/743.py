#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <queue>
#include <deque>
#include <cassert>
#include <string.h>
#include <iomanip>
using namespace std;

#define INF 1000000000
#define lint long long
#define mp make_pair
#define pb push_back

int a[30];
char g[30][30];
int f[30][30];
int n;
int gok;

void go(int wmask, int mmask)
{
	//cout << wmask << " " << mmask << endl;
	for (int i = 0; i < n; ++i)
	{
		if (wmask&(1 << i))
			continue;
		int nwmask = wmask | (1 << i);
		int ok = 0;
		//cout << i << endl;
		for (int j = 0; j < n; ++j)
		{
			if (!f[i][j])
				continue;
			//cout << "work " << (mmask&(1 << j)) << endl;
			if (mmask&(1 << j))continue;
			ok = 1;
			int nmmask = mmask | (1 << j);
			go(nwmask, nmmask);
		}
		//cout << i << " " << ok << "x\n";
		if (!ok)
		{
			gok = 0;
		}
	}
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc, T = 1;
	scanf("%d", &tc);

	while (tc--)
	{
		printf("Case #%d: ", T++);

		scanf("%d", &n);

		for (int i = 0; i < n; ++i)
		{
			a[i] = i + 1;
		}

		for (int i = 0; i < n; ++i)
		{
			scanf("%s", g[i]);
		}

		int ans = n*n;
		for (int i = 0; i < (1<<(n*n)); ++i)
		{
			int cost = 0;
			for (int j = 0; j < n; ++j)
			{
				for (int k = 0; k < n; ++k)
				{
					if (i&(1 << (j*n + k)))
					{
						f[j][k] = 1;
						if (g[j][k] == '0')
							++cost;
					}
					else if (g[j][k] == '1')
					{
						f[j][k] = 1;
					}
					else
					{
						f[j][k] = 0;
					}
					//cout << f[j][k] << " ";
				}
				//cout << endl;
			}

			//cout << cost << endl;
			gok = 1;

			go(0, 0);

			//cout << gok << "x\n";

			if (gok)
			{
				ans = min(ans, cost);
			}
		}

		printf("%d\n", ans);
	}
	return 0;
}