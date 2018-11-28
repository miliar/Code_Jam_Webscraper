#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <climits>
#include <vector>
#include <stack>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <bitset>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

#define vt vector
#define ll long long

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++)
	{
		int n;
		cin >> n;
		vt<string> inp(n);
		for(int i = 0; i < n; i++)
		{
			cin >> inp[i];
		}
		bool ans = true;
		string state = "";
		char p = ' ';
		for(int j = 0; j < inp[0].length(); j++)
			if (inp[0][j] != p)
			{
				p = inp[0][j];
				state += inp[0][j];
			}
		if (state[state.length()-1] != inp[0][inp[0].length()-1])
			state += inp[0][inp[0].length()-1];

		for(int i = 1; i < inp.size(); i++)
		{
			string pstate = "";
			char p = ' ';
			for(int j = 0; j < inp[i].length(); j++)
				if (inp[i][j] != p)
				{
					p = inp[i][j];
					pstate += inp[i][j];
				}
				if (state[state.length()-1] != inp[i][inp[i].length()-1])
					pstate += inp[i][inp[i].length()-1];
			if (pstate != state)
			{
				ans = false;
				break;
			}
		}
		if (ans)
		{
			vt< vt<int> > sol(inp.size(), vt<int>(state.length(), 0));
			for(int i = 0; i < inp.size(); i++)
			{
				int iter = 0;
				for(int j = 0; j < inp[i].length(); j++)
					if (state[iter] != inp[i][j])
					{
						iter++;
						sol[i][iter]++;
					}
					else
					{
						sol[i][iter]++;
					}
			}
			vt<int> means(state.size(), 0), sum(state.size(), 0);
			for(int i = 0; i < state.length(); i++)
				for(int j = 0; j < inp.size(); j++)
				{
					means[i]+= sol[j][i];
					sum[i]+= sol[j][i];
				}
			for(int i = 0; i < state.length(); i++)
				means[i] /= inp.size();
			vt<int> best(state.length(), INT_MAX);
			for(int i = 0; i < state.length(); i++)
				for(int j = max(means[i]-1,0); j <= means[i]+1; j++)
				{
					int val = 0;
					for(int k = 0; k < inp.size(); k++)
						val += abs(j-sol[k][i]);
					best[i] = min(best[i], val);
				}
			int oper = 0;
			for(int i = 0; i < state.length(); i++)
				oper += best[i];
			cout << "Case #" << cases << ": " << oper << endl;
		}
		else
			cout << "Case #" << cases << ": Fegla Won" << endl;

	}
	return 0;
}