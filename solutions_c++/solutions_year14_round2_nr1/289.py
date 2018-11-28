#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>
using namespace std;

#define pii pair<int,char>

vector <pii> resolve (string str)
{
	vector <pii> ret;

	char c = str[0];
	int n = 1;

	for (int i=1;i<str.size();i++)
	{
		if (str[i] != c)
		{
			pii np = pii (n, c);
			ret.push_back(np);
			c = str[i];
			n = 1;
		}
		else
			n++;
	}
	pii np = pii (n, c);
	ret.push_back(np);
	

	return ret;
}

int main ()
{
	int c;
	freopen ("A-small.in", "r", stdin);
	freopen ("A-small.out", "w", stdout);
	cin >> c;

	for (int i=1;i<=c;i++)
	{
		cout << "Case #" << i << ": ";
		
		int n;

		cin >> n;
		vector <string> v;
	
		for (int j=0;j<n;j++)
		{
			string x;
			cin >> x;
			v.push_back(x);
		}

		vector <vector <pii> > r;

		int ss = 0;
		int ret = 0;

		for (int j=0;j<n;j++)
		{
			vector <pii> p = resolve (v[j]);
			r.push_back(p);
			if (!j)
				ss = p.size();
			else if (ss != p.size())
			{
				ret = 1<<30;
				goto a;
			}
			/*for (int k=0;k<p.size();k++)
			{
				cout << p[k].first << " " << p[k].second << endl;
			}*/
		}


		

		for (int j=0;j<r[0].size();j++)
		{
			char t = r[0][j].second;
			vector <int> p;
			for (int k=0;k<n;k++)
			{
				if (r[k][j].second != t)
				{
					ret = 1<<30;
					goto a;
				}
				p.push_back(r[k][j].first);
			}
			/*cout << j << ":\n";
			for (int k=0;k<n;k++)
				cout << p[k] << " ";
			cout << endl;*/
			int mn = 1<<30;
			for (int k=1;k<=100;k++)
			{
				int res = 0;
				for (int l=0;l<n;l++)
					res += abs (k-p[l]);
				mn = min (mn, res);
			}
			ret += mn;
		}
		a:
		if (ret == (1<<30))
			cout << "Fegla Won" << endl;
		else
			cout << ret << endl;
	}

	return 0;
}
