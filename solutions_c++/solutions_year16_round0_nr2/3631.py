// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <cstring>
using namespace std;

bool IsAllPlus(string s)
{
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '-')
			return false;
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		string s;
		cin >> s;
		
		map <string, bool> done;

		queue < pair <string,int> > q;
		pair <string, int> f(s, 0);
		q.push(f);
		done[s] = true;
		while (!q.empty())
		{
			string front = q.front().first;
			int lev = q.front().second;
			q.pop();
			if (IsAllPlus(front))
			{
				cout << "Case #" << i << ": " << lev << "\n";
				break;
			}
			string p;
			for (int k = 1; k <= front.size(); k++)
			{
				p = front.substr(0, k);
				reverse(p.begin(), p.end());
				for (int j = 0; j < p.size(); j++)
				{
					if (p[j] == '-')
					{
						p[j] = '+';
					}
					else
					{
						p[j] = '-';
					}
				}
				p += front.substr(k);
				if (done.find(p) != done.end())
				{
					continue;
				}
				pair <string, int> newPair(p, lev + 1);
				done[p] = true;
				q.push(newPair);
			}
		}
	}
	return 0;
}

