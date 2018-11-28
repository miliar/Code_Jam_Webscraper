#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <list>
#include <unordered_map>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;


void p1(istream& is, ostream& os)
{
	int t;
	is >> t;
	
	for (int i = 1; i <= t; ++i)
	{
		map<int, bool> mid;
		int n;
		is >> n;
		for (int j = 0; j < (2 * n - 1) * n; j++)
		{
			int temp;
			is >> temp;
			auto it = mid.find(temp);
			if (it == mid.end())
			{
				mid[temp] = false;
			}
			else
			{
				it->second ^= true;
			}
		}
		vector<int> res;
		for (auto i : mid)
		{
			if (!i.second)
				res.push_back(i.first);
		}
		sort(res.begin(), res.end());

		os << "Case #" << i << ": ";
		for (auto i : res)
		{
			os << i << " ";
		}
		os << endl;
	}
}

int main()
{
	ifstream is;
	ofstream ofs;
	is.open("B-large.in");
	ofs.open("out.txt");
	p1(is, ofs);
	system("pause");
	return 0;
}