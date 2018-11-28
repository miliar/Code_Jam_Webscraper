#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>

using namespace std;

string t[10];
int n, m;
int best, bc;
int v[10];

int solve(vector<string> s)
{
	set<string> g;
	for (int i = 0; i < s.size(); i++)
		for (int j = 0; j <= s[i].length(); j++)
			g.insert(s[i].substr(0, j));
	return g.size();
}

void gen(int k)
{
	if (k == m)
	{
		int cur = 0;
		int fail = 0;
		for (int i = 0; i < n; i++)
		{
			vector<string> s;
			for (int j = 0; j < m; j++)
				if (v[j] == i)
					s.push_back(t[j]);
			if (s.empty())
			{
				fail = 1;
				break;
			}
			cur += solve(s);
		}
		if (fail)
			return;
		if (cur > best)
		{
			best = cur;
			bc = 1;
		}
		else if (cur == best)
			bc++;
		return;
	}
	for (int i = 0; i < n; i++)
	{
		v[k] = i;
		gen(k + 1);
	}
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	cin >> m >> n;
    	for (int i = 0; i < m; i++)
    		cin >> t[i];
    	best = 0;
    	gen(0);
    	cout << "Case #" << tc + 1 << ": " << best << " " << bc << endl;
    }
    return 0;
}