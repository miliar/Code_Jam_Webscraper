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

int maxd = 0;
bool DFS(vector<int> temp, bool *visit, int next, int begin, int d) {
	if (next == begin) { 
		maxd = max(d, maxd);
		return true;
	}

 
	if (!visit[next]) {
		visit[next] = true;  
		if (DFS(temp, visit, temp[next], begin, d + 1)) {  
				return true;
			}
		visit[next] = false;
	}
	return false;
}


void p2(istream& is, ostream& os)
{
	int t;
	is >> t;
	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		vector<int> mid;
		mid.push_back(0);
		maxd = 0;
		for (int i = 0; i < n; ++i)
		{
			int temp;
			cin >> temp;
			mid.push_back(temp);
		}

		bool *visited = new bool[n];
		memset(visited, 0, n);
		for (int i = 1; i <= n; i++)
		{
			DFS(mid, visited, mid[i], i, 1);
			memset(visited, 0, n);
		}
		os << "Case #" << i << ": " << maxd << endl;
	}
}


void p3(istream& is, ostream& os)
{
	int t;
	is >> t;
	for (int i = 1; i <= t; ++i)
	{
		string s;
		is >> s;
		string temp;
		temp.insert(temp.begin(), 1, s[0]);
		for (unsigned j = 1; j < s.size(); j++)
		{
			if (s[j] >= *(temp.begin()))
				temp.insert(temp.begin(), 1, s[j]);
			else temp.insert(temp.end(), 1, s[j]);
		}
		os << "Case #" << i << ": " << temp << endl;
	}
}


int main()
{
	ifstream is;
	ofstream ofs;
	is.open("A-large.in");
	ofs.open("out.txt");
	//p2(cin, cout);
	p3(is, ofs);
	system("pause");
	return 0;
}