#include <vector>
#include <cstring>
#include <queue>
#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
using namespace std;

int n, m;
int a[110][110], tem[110][110], mxr[110], mxc[110];

string f()
{
	for (int i = 0; i < n; i++)
	{
		mxr[i] = a[i][0];
		for (int j = 0; j < m; j++)
			if (a[i][j] > mxr[i])	mxr[i] = a[i][j];
	}
	for (int j = 0; j < m; j++)
	{
		mxc[j] = a[0][j];
		for (int i = 0; i < n; i++)
			if (a[i][j] > mxc[j])	mxc[j] = a[i][j];
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if (!(a[i][j] >= mxr[i] || a[i][j] >= mxc[j]))
				return "NO";
		}
	return "YES";
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;		cin >> tc;
	for (int T = 1; T <= tc; T++)
	{
		cin >> n >> m;
		for (int i =0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j];
		cout << "Case #" << T << ": " << f() << endl;
	}
}