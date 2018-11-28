#include <bits/stdc++.h>

using namespace std;

unordered_map<string, bool> mark;
unordered_map<string, int> dis;
vector<string> q;

string convert(string s)
{
	string ret = s.substr(0, 1);
	for (int i = 1; i < s.length(); i++)
		if (s[i] != ret[ret.length() - 1])
			ret += s[i];
	return ret;
}

string rev(string s, int idx)
{
	string ret = s;
	for (int i = 0; i <= idx; i++)
		ret[i] = ((s[idx - i] == '+') ? '-' : '+');
	return ret;
}

int bfs(string st)
{
	mark.clear();
	dis.clear();
	q.clear();
	st = convert(st);
	dis[st] = 0;
	mark[st] = true;
	q.push_back(st);
	for (int i = 0; i < q.size(); i++)
	{
		string v = q[i];
		mark[v] = true;
		if (v == "+")
			return dis[v];
		for (int j = 0; j < v.length(); j++)
		{
			string u = convert(rev(v, j));
			if (!mark[u])
			{
				mark[u] = true;
				dis[u] = dis[v] + 1;
				q.push_back(u);
			}
		}
	}
}

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;
		cout << "Case #" << tt << ": " << bfs(s) << endl;
	}
	return 0;
}