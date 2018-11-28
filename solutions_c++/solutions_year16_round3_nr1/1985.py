#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <queue>
#include <cassert>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <set>

using namespace std;

bool valid(vector<int>&c)
{
	int max = 0, max_i = -1, sum = 0;
	for (int i = 0; i < c.size(); i++)
	{
		sum += c[i];
		max = c[i] > max ? c[i] : max;
	}
	if (max == 1 && sum == 2) 
		return false;
	for (int i = 0; i < c.size(); i++)
	{
		if (c[i])
			if (double(c[i] - 1) / double(sum - 1) > .5)
				return false;
	}
	return true;
}


int main()
{
#if _JOE_PC
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int ncase; cin >> ncase;
	for (int icase = 1; icase <= ncase; icase++)
	{
		cout << "Case #" << icase << ": ";
		int n; cin >> n;
		vector<int> counts(n);
		for (int i = 0; i < n; i++) cin >> counts[i];
		bool done = false;
		while (!done)
		{
			
			int max = 0;
			int max_i = -1;
			for (int i = 0; i < n; i++)
			{
				if (counts[i] > max)
				{
					max = counts[i];
					max_i = i;

				}
			}
			if (max == 0)
			{
				done = true; break;
			}
			cout << char('A' + max_i);
			counts[max_i]--;
			max = 0;
			max_i = -1;
			for (int i = 0; i < n; i++)
			{
				if (counts[i] > max)
				{
					max = counts[i];
					max_i = i;
				}
			}
			if (valid(counts))
			{
				counts[max_i]--;
				cout << char('A' + max_i);
			}
			cout << " ";


		}
		cout << endl;

	}

}