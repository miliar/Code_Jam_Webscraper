#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

void SortS(string& s)
{
	for (unsigned w = 2; w <= s.size(); w *= 2)
	{
		for (unsigned i = 0; i * w < s.size(); ++i)
		{
			bool sr = false;
			for (unsigned j = 0; j < w / 2; ++j)
			{
				if (s[i * w + j] < s[i * w + j + w / 2]) break;
				if (s[i * w + j] > s[i * w + j + w / 2])
				{
					sr = true;
					break;
				}
			}
			if (sr)
			{
				for (unsigned j = 0; j < w / 2; ++j)
				{
					swap(s[i * w + j], s[i * w + j + w / 2]);
				}
			}
		}
	}
}

int main()
{
	vector<vector<string>> vs;
	vs.resize(1, { "P", "R", "S" });
	for (; vs.size() <= 12; )
	{
		vector<string> vst;
		for (unsigned i = 0; i < 3; ++i)
		{
			string s;
			s.reserve(vs.back()[i].size() * 2);
			for (char c : vs.back()[i])
			{
				if (c == 'P') 
				{
					s.push_back('P'); s.push_back('R');
				}
				else if (c == 'R')
				{
					s.push_back('S'); s.push_back('R');
				}
				else if (c == 'S')
				{
					s.push_back('P'); s.push_back('S');
				}
			}
			SortS(s);
			vst.push_back(s);
		}
		vs.push_back(vst);
	}
	vector<vector<vector<unsigned>>> vsc;
	vsc.resize(vs.size(), vector<vector<unsigned>>(3, vector<unsigned>(3, 0)));
	for (unsigned i = 0; i < vs.size(); ++i)
	{
		for (unsigned j = 0; j < 3; ++j)
		{
			for (char c : vs[i][j])
			{
				if (c == 'P') vsc[i][j][0]++;
				if (c == 'R') vsc[i][j][1]++;
				if (c == 'S') vsc[i][j][2]++;
			}
		}
	}
	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		cout << "Case #" << it + 1 << ": ";
		uint64_t N, P, R, S;
		cin >> N >> R >> P >> S;
		bool find = false;
		for (unsigned i = 0; i < 3; ++i)
		{
			if ((P == vsc[N][i][0]) && (R == vsc[N][i][1]) && (S == vsc[N][i][2]))
			{
				find = true;
				cout << vs[N][i];
				break;
			}
		}
		if (!find) cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
