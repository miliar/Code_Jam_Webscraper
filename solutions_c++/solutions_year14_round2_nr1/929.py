#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <climits>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define wait system("pause")

int main()
{
	ifstream in("A-large.in");
	ofstream out("a.out");
	int t;
	in >> t;
	REP1(II, t)
	{
		out << "Case #" << II << ": ";
		int n;
		in >> n;
		vector<string> a(n);
		vector<char> mask[105];
		vector<int> len[105];
		REP(i, n)
			in >> a[i];
		
		REP(i, n)
		{
			mask[i].push_back(a[i][0]);
			len[i].push_back(1);
			for (int j = 0; j < a[i].size() - 1; j++)
			{
				if (a[i][j] != a[i][j + 1])
				{
					mask[i].push_back(a[i][j + 1]);
					len[i].push_back(1);
				}
				else
				{
					len[i][len[i].size() - 1] ++;
				}

			}
		}
		bool ok = true;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (mask[i] != mask[j])
				{
					ok = false;
					i = n;
					j = n;
					break;
				}
			}
		}
		if (!ok)
		{
			out << "Fegla Won";
		}
		else
		{
			ll ans = 0;
			for (int i = 0; i < len[0].size(); i++)
			{
				ll qq = LLONG_MAX;
				for (int j = 0; j < n; j++)
				{
					ll ms = 0;// len[j][i];
					for (int g = 0; g < n; g++)
					{
						ms += abs(len[g][i] - len[j][i]);
					}
					qq = min(qq, ms);
				}
				ans += qq;
			}
			out << ans;
		}
		out << "\n";
	}
	in.close();
	out.close();
	return 0;
}