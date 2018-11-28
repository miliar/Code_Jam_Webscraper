#include <vector>
#include <algorithm>
#include<set>
#include <fstream>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

vector<string> mat;
vector<vector<bool> > tk;
int dfs(int i, int j, int dx, int dy)
{
	if (i < 0 || i >= mat.size() || j < 0 || j >= mat[0].size()) return 1;
	if (tk[i][j]) return 0;
	if (mat[i][j] != '.')
	{
		tk[i][j] = true;
		if (mat[i][j] == '<')
		{
			dy = -1;
			dx = 0;
		}
		else if (mat[i][j] == '^')
		{
			dx = -1;
			dy = 0;
		}
		else if (mat[i][j] == 'v')
		{
			dx = 1;
			dy = 0;
		}
		else
		{
			dx = 0;
			dy = 1;
		}
	}
	return dfs(i+dx, j + dy, dx, dy);
	
}
int main()
{

	ifstream cin;
	ofstream cout;
	cin.open("in.in");
	cout.open("out.out");
	
	
	int T;
	cin>>T;
	for (int z = 1; z <= T; z++)
	{
		int R, C;
		cin>>R>>C;
		mat = vector<string>(R);
		for (int i = 0; i < R; i++) cin>>mat[i];
		vector<int> rows(R, 0);
		vector<int> cols(C, 0);
		tk = vector<vector<bool> >(R, vector<bool> (C, false));
		for (int i = 0; i <R; i++) for (int j = 0; j < C; j++)
		{
			if (mat[i][j] != '.')
			{
				rows[i]++;
				cols[j]++;
			}
		}
		bool ok = true;
		for (int i = 0; i <R; i++) for (int j = 0; j < C; j++)
		{
			if (mat[i][j] != '.')
			{
				if (rows[i] == 1 && cols[j] == 1)
				{
					ok = false;
				}
			}
		}
		if (!ok)
		{
			cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int r = 0;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++) if (mat[i][j] != '.')
			{
				r += dfs(i, j, 0, 0);
			}
		}
		cout<<"Case #"<<z<<": "<<r<<endl;
	}
}