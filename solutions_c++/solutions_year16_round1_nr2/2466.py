#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define INF mod
#define pi acos(-1.0)
#define LINF 1000000000000000000LL
#define eps 1e-10
/*
string solve(string s)
{
	if(s.size() <= 1)
		return s;
	int pos = max_element(s.begin(), s.end()) - s.begin();
	string res = solve(s.substr(0, pos));
	for(int i = pos; i < s.size(); i++)
		if(s[i] == s[pos])
			res = s[i] + res;
	for(int i = pos; i < s.size(); i++)
		if(s[i] != s[pos])
			res += s[i];
	return res;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		string res = solve(s);
		printf("Case #%d: %s\n", t, res.c_str());
	}
	return 0;
}
*/

int b[55][55], used[105], used2[105];
vector<vector <int> > a;
vector <int> column;
int n;
bool solved;

void solve(int row, int i)
{
	if(solved)
		return;
	if(row == n)
	{
		for(int j = 0; j < 2 * n - 1; j++)
			used2[j] = used[j];
		int cnt = 0, absent = -1;
		for(int j = 0; j < n; j++)
		{
			for(int k = 0; k < n; k++)
				column[k] = b[k][j];
			int pos = lower_bound(a.begin(), a.end(), column) - a.begin();
			if(a[pos] == column && used2[pos])
			{
				if(pos + 1 < 2 * n - 1 && used2[pos+1] == 0 && a[pos] == a[pos+1])
					pos++;
			}
			if(pos == 2 * n - 1 || used2[pos] || a[pos] != column)
			{
				cnt++;
				absent = j;
			}
			if(a[pos] == column)
				used2[pos] = 1;
			if(cnt > 1)
				return;
		}
		for(int j = 0; j < n; j++)
			printf(" %d", b[j][absent]);
		puts("");
		solved = true;
		return;
	}
	if(i >= 2 * n - 1)
		return;
	//if(a[i][row] == b[row][row])
	{
		bool ok = true;
		if(row > 0)
		{
			for(int j = 0; j < n; j++)
				if(b[row-1][j] >= a[i][j])
				{
					ok = false;
					break;
				}
		}
		if(ok)
		{
			used[i] = 1;
			for(int j = 0; j < n; j++)
				b[row][j] = a[i][j];
			solve(row + 1, i + 1);
			used[i] = 0;
		}
	}
	solve(row, i + 1);
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		solved = false;
		printf("Case #%d:", t);
		scanf("%d", &n);
		a.resize(2 * n - 1);
		column.resize(n);
		for(int i = 0; i < 2 * n - 1; i++)
		{
			a[i].resize(n);
			for(int j = 0; j < n; j++)
				scanf("%d", &a[i][j]);
		}
		sort(a.begin(), a.end());
		memset(used, 0, sizeof(used));
		solve(0, 0);
	}
	return 0;
}