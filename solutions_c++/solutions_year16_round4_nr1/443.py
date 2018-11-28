#include <cstdio>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
using namespace std;

int n;


string res(char x,int move)
{
	if (move == n)
	{
		string r = "";
		r += x;
		return r;
	}
	string h1 = res(x, move + 1);
	string h2;
	if (x == 'R')
	{
		h2 = res('S', move + 1);
	}
	if (x == 'S')
		h2 = res('P', move + 1);
	if (x == 'P')
		h2 = res('R', move + 1);
	if (h1 < h2)
		return h1 + h2;
	return h2 + h1;
}

int r, s, p;

bool check(string res)
{
	int r1 = 0, s1 = 0, p1 = 0;
	for (int i = 0; i < res.length(); i++)
	{
		if (res[i] == 'R')
			r1++;
		if (res[i] == 'S')
			s1++;
		if (res[i] == 'P')
			p1++;
	}
	if (r != r1)
		return false;
	if (s != s1)
		return false;
	if (p != p1)
		return false;
	return true;
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qq;
	cin >> qq;
	for (int qqq = 0; qqq < qq; qqq++)
	{
		cout << "Case #" << qqq + 1 << ": ";
		cin >> n;
		cin >> r >> p >> s;
		vector <string> ans;
		if (check(res('P', 0)))
		{
			ans.push_back(res('P', 0));	
		}
		if (check(res('S', 0)))
		{
			ans.push_back(res('S', 0));

		}
		if (check(res('R', 0)))
		{
			ans.push_back(res('R', 0));
		}
		if (ans.size() == 0)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			sort(ans.begin(), ans.end());
			for (int i = 0; i < ans[0].length();i++)
			cout << ans[0][i];
			cout << endl;
		}

	}
	return 0;
}