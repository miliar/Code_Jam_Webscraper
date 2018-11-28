#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
#include<bitset>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned int ui;
#define mp make_pair

namespace
{
	int n;
	ui g[32];

	int numFree;
	vector<pii> vWM;

	pii currentCheck[32];

	int cnt(ui x)
	{
		return bitset<32>(x).count();
	}

	int result;
	void update(ui& uOld, ui uNew)
	{
		result += cnt(uNew) - cnt(uOld);
		uOld = uNew;
	}

	vector<int> parent;
	int go(int i)
	{
		if (i == vWM.size())
		{
			int totalInitialCost = 0;
			for (int i = 0; i < vWM.size(); ++i)
			{
				totalInitialCost += vWM[i].first * vWM[i].second;
			}

			copy(vWM.begin(), vWM.end(), currentCheck);
			for (int j = 0; j < vWM.size(); ++j)
			{
				if (parent[j] > -1)
				{
					currentCheck[parent[j]].first += currentCheck[j].first;
					currentCheck[parent[j]].second += currentCheck[j].second;
				}
			}

			int totalFinalCost = 0;
			int freeWorkersUsed = 0;
			for (int j = 0; j < vWM.size(); ++j)
			{
				if (parent[j] == -1)
				{
					int numWorkers = currentCheck[j].first;
					int numMachines = currentCheck[j].second;
					
					int costMult = max(numWorkers, numMachines);
					totalFinalCost += costMult * costMult;

					if (numWorkers < numMachines)
						freeWorkersUsed += numMachines - numWorkers;
				}
			}

			if (freeWorkersUsed > numFree)
				return 1000000;

			int result = totalFinalCost - totalInitialCost;
			result += (numFree - freeWorkersUsed); // 1 each for the rest
			return result;
		}
		
		parent[i] = -1;
		int ret = go(i + 1);

		// try possible parents
		for (int j = 0; j < i; ++j)
		{
			if (parent[j] == -1)
			{
				parent[i] = j;
				int thisResult = go(i + 1);
				ret = min(ret, thisResult);
			}
		}

		return ret;
	}

}

//int main16R2_D()
int main()
{
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");
	//ifstream fin("test.in");
	//ofstream fout("test.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz = 1; zz <= numberOfCases; ++zz)
	{
		fin >> n;

		result = 0;
		numFree = 0;
		memset(g, 0, sizeof(g));

		for (int i = 0; i < n; ++i)
		{
			string s;
			fin >> s;
			for (int j = 0; j < n; ++j)
			{
				if (s[j] == '1')
					g[i] |= (1 << j);
			}
		}

		set<ui> seen;

		vWM.clear();
		for (int i = 0; i < n; ++i)
		{
			if (seen.count(g[i]) > 0) continue;
			if (g[i] == 0)
			{
				++numFree;
				continue;
			}

			bool updated = true;
			while (updated)
			{
				updated = false;
				for (int j = i + 1; j < n; ++j)
				{
					if (g[i] == g[j]) continue;
					if ((g[i] & g[j]) == 0) continue;

					ui newMask = g[i] | g[j];
					update(g[i], newMask);
					update(g[j], newMask);
					updated = true;
				}
			}

			int numWorkers = count(g, g + n, g[i]);
			int numMachines = cnt(g[i]);

			if (numWorkers != numMachines)
			{
				vWM.push_back(make_pair(numWorkers, numMachines));
			}
			
			seen.insert(g[i]);
		}

		parent.resize(n);
		int extra = go(0);
		result += extra;
		fout << "Case #" << zz << ": " << result << endl;

	}

	return 0;
}
