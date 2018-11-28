#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <stdint.h>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)


int main()
{
	int numCases;
	cin >> numCases;

	forl(caseNo, 1, numCases+1)
	{
		int numBlocks;
		cin >> numBlocks;
		set<double> naomiBlocks;
		set<double> kenBlocks;

		forl(i,0,numBlocks)
		{
			double tmp;
			cin >> tmp;
			naomiBlocks.insert(tmp);
		}
		forl(i,0,numBlocks)
		{
			double tmp;
			cin >> tmp;
			kenBlocks.insert(tmp);
		}

		// Play war.
		set<double> nwBlocks = naomiBlocks;
		set<double> kwBlocks = kenBlocks;
		int nwWins = 0;
		forl(i,0,numBlocks)
		{
			double nblock = *(nwBlocks.begin());
			nwBlocks.erase(nwBlocks.begin());
			// If Ken has a block > Naomi's.
			if (kwBlocks.lower_bound(nblock) != kwBlocks.end())
			{
				// Play the smallest block bigger than hers.
				kwBlocks.erase(kwBlocks.lower_bound(nblock));
			}
			else
			{
				// Lose, but only discard your smallest block.
				kwBlocks.erase(kwBlocks.begin());
				nwWins++;
			}
		}

		// Play Deceitful War.

		int nWins = 0;
		forl(i,0,numBlocks)
		{
			double kenSmallest = *(kenBlocks.begin());
			if (naomiBlocks.lower_bound(kenSmallest) != naomiBlocks.end())
			{
				// Naomi has a block > Ken's smallest block.
				// Claim that it's infinitely huge.
				// Ken will spend his smallest block on it.
				naomiBlocks.erase(naomiBlocks.lower_bound(kenSmallest));
				kenBlocks.erase(kenBlocks.begin());
				nWins++;
			}
			else
			{
				// Naomi has no blocks > Ken's smallest block, so she will always lose.
				break;
			}
		}

		cout << "Case #" << caseNo << ": " << nWins << " " << nwWins << endl;

	}
	return 0;
}
