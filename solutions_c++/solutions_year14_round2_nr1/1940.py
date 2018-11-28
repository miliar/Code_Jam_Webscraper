#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>

#define INF 2e9
#define mp make_pair
#define pb push_back

using namespace std;

int n;

int s[1000][1000];
string cs;

int get_ans(int m)
{
	int res = 0;
	int res2, ti;
	for (int i = 0; i < m; i++)
	{
		res2 = INF;
		for (int j = 0; j < n; j++)
		{
			ti = 0;
			for (int k = 0; k < n; k++)
			{
				ti += abs(s[j][i] - s[k][i]);
			}
			res2 = min(res2, ti);
		}
		res += res2;
	}
	return res;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc;
	cin >> tc;
	string tst;
	int ctr, ctr2;
	for (int ts = 0; ts < tc; ts++)
	{
		cout << "Case #" << ts + 1 << ": ";
		cin >> n;
		getline(cin, tst);
		getline(cin, tst);
		cs = "";
		for (int j = 0; j < tst.size(); j++)
		{
			cs += tst[j];
			ctr = 1;
			j++;
			while (tst[j] == tst[j - 1] && j < tst.size())
			{
				j++;
				ctr++;
			}
			s[0][cs.size() - 1] = ctr;
			j--;
		}
		for (int i = 1; i < n; i++)
		{
			getline(cin, tst);
			ctr2 = 0;
			for (int j = 0; j < tst.size(); j++)
			{
				if (cs[ctr2] != tst[j]) 
				{
					cout << "Fegla Won";
					goto cont;
				}
				ctr = 1;
				j++;
				while (tst[j] == tst[j - 1] && j < tst.size())
				{
					j++;
					ctr++;
				}
				j--;
				s[i][ctr2] = ctr;
				ctr2++;
			}
			if (ctr2 != cs.size())
			{
				cout << "Fegla Won";
				goto cont;
			}
		}
		cout << get_ans(cs.size());
cont:	cout << endl;
	}
	return 0;
}