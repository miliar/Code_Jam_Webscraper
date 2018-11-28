#ifndef CANT_USE_TEMPLATE
#define  _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

#define MP make_pair
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()
#define sqr(x) ((x)*(x))
#endif

#define  TASK ""

const int N = 100;
int n, m;
int a[N][N];
bool used[N][N];

bool can()
{
	memset(used, false, sizeof(used));
	while (1)
	{
		int I = -1, J = -1;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!used[i][j] && (I == -1 || a[I][J] > a[i][j]))
					I = i, J = j;
		if (I == -1)
			break;
		bool f1 = false;
		for (int i = 0; i < n; i++)
			if (a[i][J] > a[I][J])
			{
				f1 = true;
				break;
			}
		if (!f1)
			for (int i = 0; i < n; i++)
				used[i][J] = true;
		bool f2 = false;
		for (int j = 0; j < m; j++)
			if (a[I][j] > a[I][J])
			{
				f2 = true;
				break;
			}
		if (!f2)
			for (int j = 0; j < m; j++)
				used[I][j] = true;
		if (f1 && f2)
			return false;
	}
	return true;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(TASK ".in", "r", stdin);
	//freopen(TASK ".out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int k = 0; k < t; k++)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				cin >> a[i][j];
		cout << "Case #" << k + 1 << ": " << (can() ? "YES" : "NO") << endl;
	}
	return 0;
}