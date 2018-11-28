#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;

void print()
{

}

string mynext(string s)
{
	string ret = "";
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == 'P')
		{
			ret += "PR";
		}
		else if (s[i] == 'R')
		{
			ret += "SR";
		}
		else
		{
			ret += "PS";
		}
	}
	return ret;
}

void change(string &s)
{
	for (int i = 0; i < s.length(); i += 2)
	{
		if (s[i] == 'S' && s[i + 1] == 'R')
		{
			swap(s[i], s[i + 1]);
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		int N, R, P, S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		vector<string> s = { "PS", "SP", "PR", "RP", "RS", "SR" };
		string ret = "";
		bool imp = true;
		for (int i = 0; i < s.size(); i++)
		{
			string ss = s[i];
			for (int j = 1; j < N; j++)
			{
				ss = mynext(ss);
			}
			change(ss);
			int cntR = 0, cntP = 0, cntS = 0;
			for (int j = 0; j < ss.length(); j++)
			{
				if (ss[j] == 'R') cntR++;
				else if (ss[j] == 'P') cntP++;
				else cntS++;
			}
			if (cntR == R && cntP == P && cntS == S)
			{
				if (imp)
				{
					imp = false;
					ret = ss;
				}
				else if (ss<ret)
				{
					ret = ss;
				}
			}
		}
		if(!imp) cout << "Case #" << cases << ": " << ret << endl;
		else cout << "Case #" << cases << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}