#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

typedef long long ll;

map<int, int> ms;

void calc(vector<vector<string>> sd)
{
    int c = 0;
    for (int i = 0; i < sd.size(); ++i)
    {
        set<string> st;
        if (sd[i].size() == 0)
            return;
        for (int j = 0; j < sd[i].size(); ++j)
        {
            for (int k = 0; k < sd[i][j].size(); ++k)
            {
                st.insert(sd[i][j].substr(0, k + 1));
            }
        }
        c += st.size() + 1;
    }
    ms[c]++;
}

void rec(vector<string> d, vector<vector<string>> sd, int c)
{
    if (c == d.size())
        calc(sd); 
    else
    {
        for (int i = 0; i < sd.size(); ++i)
        {
            sd[i].push_back(d[c]);
            rec(d, sd, c + 1);
            sd[i].pop_back();
        }
    }
}

void solve()
{
    ms.clear();
	int n, m;
    cin >> m >> n;
    vector<string> d(m);
    for (int i = 0; i < m; ++i)
        cin >> d[i];
    vector<vector<string>> sd(n);
    rec(d, sd, 0);
    cout << ms.rbegin()->first << " " << ms.rbegin()->second;
}

void main()
{
	freopen("i.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}