#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <unordered_map>
using namespace std;

unordered_map<long long, string> h;

string solve(string s)
{
	if (s.size() > 2)
	{
		string s1 = solve(string(s, 0, s.size() / 2)), s2 = solve(string(s, s.size() / 2, s.size() / 2));
		if (s1 > s2)
			return s2 + s1;
		return s1 + s2;
	}
	return s;
}

int main()
{
	vector<long long> v;
	h[10001] = "PS";
	v.push_back(10001);
	h[100000001] = "RS";
	v.push_back(100000001);
	h[100010000] = "PR";
	v.push_back(100010000);
	while (v.size() > 0)
	{
		long long l = v.back();
		v.pop_back();
		long long r = l / 100000000;
		long long p = (l % 100000000) / 10000;
		long long s = l % 10000;
		if (r + p + s < 4096)
		{
			long long nr = r + p, np = p + s, ns = s + r;
			string str = h[l], nstr = str + str;
			for (int i = 0; i < str.length(); ++i)
			{
				if (str[i] == 'P')
				{
					nstr[i*2] = 'P';
					nstr[i*2+1] = 'R';
				}
				else if (str[i] == 'R')
				{
					nstr[i*2] = 'R';
					nstr[i*2+1] = 'S';
				}
				else
				{
					nstr[i*2] = 'P';
					nstr[i*2+1] = 'S';
				}
			}
			long long nid = nr * 100000000 + np * 10000 + ns;
			v.push_back(nid);
			if (h.find(nid) != h.end())
				cout << "!!!" << nid << endl;
			h[nid] = nstr;
		}
	}
	
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		long long n, r, p, s;
		cin >> n >> r >> p >> s;
		if (h.find(r * 100000000 + p * 10000 + s) != h.end())
			cout << "Case #" << tt << ": " << solve(h[r * 100000000 + p * 10000 + s]) << endl;
		else
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
