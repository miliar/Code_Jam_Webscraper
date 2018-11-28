#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>
#include <map>
#include<cassert> 
using namespace std;

typedef pair<string, string> topic;

void testcase()
{
	int n;
	cin >> n;

	vector<topic> ts(n);
	vector<pair<bool, bool>> dupl(n, pair<bool, bool>(false,false));

	map<string, vector<int>> freq1,freq2;

	for (int i = 0; i < n; ++i)
	{
		string s1, s2;
		cin >> s1 >> s2;
		ts[i].first = s1; ts[i].second = s2;

		freq1[s1].push_back(i);
		freq2[s2].push_back(i);

		if (freq1[s1].size() > 1)
		{
			for (auto ind : freq1[s1])
			{
				dupl[ind].first = true;
			}
		}

		if (freq2[s2].size() > 1)
		{
			for (auto ind : freq2[s2])
			{
				dupl[ind].second = true;
			}
		}
	}

	int res = 0;

	vector<int> duplind;
	int dqt = 0;
	for (int i = 0; i < dupl.size(); ++i)
		if (dupl[i].first && dupl[i].second)
			duplind.push_back(i);

	
	vector<int> cur(duplind.size(), 0);
	auto dupl1 = dupl;
	auto freq11 = freq1;
	auto freq22 = freq2;

	for( int i = 0 ; i < dupl.size(); ++i)
	{ 
		if (dupl[i].first && dupl[i].second)
		{
			res++;

			string s1 = ts[i].first, s2 = ts[i].second;

			auto& col1 = freq1[s1];
			auto it1 = find(col1.begin(), col1.end(), i);
			assert(it1 != col1.end());
			col1.erase(it1);
			if (col1.size() == 1)
			{
				dupl[col1[0]].first = false;
			}

			auto& col2 = freq2[s2];
			auto it2 = find(col2.begin(), col2.end(), i);
			assert(it2 != col2.end());
			col2.erase(it2);
			if (col2.size() == 1)
			{
				dupl[col2[0]].second = false;
			}

		}
	}

	int maxnum = (1 << duplind.size());

	for (int k = 0; k < maxnum; ++k)
	{
		int cursum = 0;
		for (int j = 0; j < 31; ++j)
		{
			if (((1 << j) & k))
				cursum++;
		}
		if (cursum < res)
			continue;

		dupl = dupl1;
		freq1 = freq11;
		freq2 = freq22;

		bool succ = true;
		for (int j = 0; j < 31 && succ; ++j)
		{
			if (!((1 << j) & k))
				continue;

			int i = duplind[j];

			//if (dupl[i].first && dupl[i].second)
			{

				string s1 = ts[i].first, s2 = ts[i].second;

				auto& col1 = freq1[s1];
				if (col1.size() == 1)
				{
					succ = false;
					break;
				}
				auto it1 = find(col1.begin(), col1.end(), i);
				assert(it1 != col1.end());
				col1.erase(it1);

				auto& col2 = freq2[s2];
				if (col2.size() == 1)
				{
					succ = false;
					break;
				}
				auto it2 = find(col2.begin(), col2.end(), i);
				assert(it2 != col2.end());
				col2.erase(it2);
			}
		}

		if (succ)
			res = cursum;


	}

	cout << res << endl;
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}