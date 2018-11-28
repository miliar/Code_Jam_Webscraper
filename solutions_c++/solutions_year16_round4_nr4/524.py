#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stdio.h>
#include <string>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int getWorkerMask(int mask, int worker, int n)
{
	return (mask >> (worker * n)) & ((1 << n) - 1);
}

int getMaskCount(int mask)
{
	int count = 0;
	while (mask > 0)
	{
		count++;
		mask = mask & (mask - 1);
	}

	return count;
}

int main()
{
	cin.sync_with_stdio(0);
	freopen( "..\\input.txt", "r", stdin );
	freopen( "..\\output.txt", "w", stdout );

	int t;
	cin >> t;
	for( int tt = 1; tt <= t; tt++ )
	{
	
		int n;
		cin >> n;
		int startMask = 0;
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			for (int j = 0; j < n; j++)
			{
				if (s[j] == '1')
				{
					startMask = startMask | (1 << (i * n + j));
				}
			}
		}

		int bestAns = n * n;
		vector<int> workersMask(n);

		for (int costMask = 0; costMask < (1 << n * n); costMask++)
		{
			if ((costMask & startMask) != 0)
			{
				continue;
			}

			bool hasSol = true;

			int mask = costMask | startMask;

			int allWorkers = 0;
			for (int i = 0; i < n; i++)
			{
				workersMask[i] = getWorkerMask(mask, i, n);
				allWorkers |= workersMask[i];
			}

			if (allWorkers != ((1 << n) - 1))
			{
				continue;
			}

			for (int i = 0; i < n; i++)
			{
				int curMask = workersMask[i];
				for (int j = 0; j < n; j++)
				{
					for (int k = 0; k < n; k++)
					{
						if (curMask & workersMask[k])
						{
							curMask = curMask | workersMask[k];
						}
					}
				}

				int curMaskCount = getMaskCount(curMask);
				int wCount = 0;
				for (int j = 0; j < n; j++)
				{
					if ((curMask & workersMask[j]) == 0)
					{
						continue;
					}
					wCount++;
					if (curMask != workersMask[j])
					{
						hasSol = false;
						break;
					}
				}
				if (wCount != curMaskCount)
				{
					hasSol = false;
					break;
				}
			}

			if (!hasSol)
			{
				continue;
			}

			bestAns = min(bestAns, getMaskCount(costMask));
		}

		//printf( "Case #%d: ", tt );
		cout << "Case #" << tt << ": " << bestAns << endl;
	}
	return 0;
}