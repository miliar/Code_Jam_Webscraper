#include <iostream>
#include <string>
#include <unordered_map> 
#include <vector>
#include <cstring>
using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	// freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int k = 1; k <= T; k++)
	{
		string str;
		cin >> str;
		vector<int> v(26, 0);
		for (auto x:str)
		{
			v[x-'A'] ++;
		}
		std::vector<int> res;
		if (v[25] != 0)
		{
			int t = v[25];
			for (int i = 0; i < t; i++)
			{
				res.push_back(0);
				v[25]--;
				v['E'-'A']--;
				v['R'-'A']--;
				v['O'-'A']--;
			}
		}
		if (v['X'-'A'] != 0)
		{
			int t = v['X'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(6);
				v['S'-'A'] --;
				v['I'-'A'] --;
				v['X'-'A'] --;
			}
		}
		if (v['S'-'A'] != 0)
		{
			int t = v['S'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(7);
				v['S'-'A'] --;
				v['E'-'A'] -=2;
				v['V'-'A'] --;
				v['N'-'A'] --;
			}
		}
		if (v['G'-'A'] != 0)
		{
			int t = v['G'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(8);
				v['E'-'A'] --;
				v['I'-'A'] --;
				v['G'-'A'] --;
				v['H'-'A'] --;
				v['T'-'A'] --;
			}
		}
		if (v['V'-'A'] != 0)
		{
			int t = v['V'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(5);
				v['F'-'A'] --;
				v['I'-'A'] --;
				v['V'-'A'] --;
				v['E'-'A'] --;
			}
		}
		if (v['F'-'A'] != 0)
		{
			int t = v['F'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(4);
				v['F'-'A'] --;
				v['O'-'A'] --;
				v['U'-'A'] --;
				v['R'-'A'] --;
			}
		}
		if (v['R'-'A'] != 0)
		{
			int t = v['R'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(3);
				v['T'-'A'] --;
				v['H'-'A'] --;
				v['R'-'A'] --;
				v['E'-'A'] -=2;
			}
		}
		if (v['T'-'A'] != 0)
		{
			int t =v['T'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(2);
				v['T'-'A'] --;
				v['W'-'A'] --;
				v['O'-'A'] --;
			}
		}
		if (v['O'-'A'] != 0)
		{
			int t = v['O'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(1);
				v['O'-'A'] --;
				v['N'-'A'] --;
				v['E'-'A'] --;
			}
		}
		if (v['I'-'A'] != 0)
		{
			int t = v['I'-'A'];
			for (int i = 0; i < t; i++)
			{
				res.push_back(9);
			}
		}
		sort(res.begin(), res.end());
		cout << "Case #" << k <<": " ;
		for (auto x:res)
		{
			cout << x ;
		}
		cout << endl;
	}
	return 0;
}