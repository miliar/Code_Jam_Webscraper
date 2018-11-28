#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <list>
#include <set>
using namespace std;

void readBlock(int number, vector<double>& blocks)
{
	double value;
	for (int i = 0; i < number; ++i)
	{
		scanf("%lf", &value);
		blocks.push_back(value);
	}
}

pair<int, int> solve(vector<double>& naomiBlocks, vector<double>& kenBlocks)
{
	pair<int, int> result(0, 0);
	sort(naomiBlocks.begin(), naomiBlocks.end());
	sort(kenBlocks.begin(), kenBlocks.end());
	set<double> setOfKenBlocks(kenBlocks.begin(), kenBlocks.end());

	for (int blockNumber = 0; blockNumber < naomiBlocks.size(); ++blockNumber)
	{
		set<double>::iterator it = setOfKenBlocks.upper_bound(naomiBlocks[blockNumber]);

		if (it == setOfKenBlocks.end())
		{
			result.second += naomiBlocks.size() - blockNumber;
			break;
		}
		else
		{
			setOfKenBlocks.erase(it);
		}
	}

	int pointer = 0;
	for (int i = 0; i < naomiBlocks.size(); ++i)
	{
		if (naomiBlocks[i] > kenBlocks[pointer])
		{
			result.first++;
			pointer++;
		}
	}
	return result;
}

int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int testCase = 1; testCase <= testCases; ++testCase)
	{
		int blocks;
		scanf("%d", &blocks);
		vector<double> naomiBlocks, kenBlocks;
		readBlock(blocks, naomiBlocks);
		readBlock(blocks, kenBlocks);
		pair<int, int> points = solve(naomiBlocks, kenBlocks);
		printf("Case #%d: %d %d\n", testCase, points.first, points.second);
		
	}
	return 0;
}
