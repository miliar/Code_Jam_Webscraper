#define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>
#include <memory.h>

using namespace std;

#pragma comment (linker, "/STACK:64000000")

#define INF 1234567890

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned int uint;

struct p3d
{
	int x, y, z;
	p3d(int _x, int _y, int _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}
};

struct p3d_d
{
	double x, y, z;
	p3d_d(double _x, double _y, double _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}
};

int64 C(int n, int k = 4)
{
	if (n < k)
		return 0;

	int64 res = 1;
	for (int i = n; i > n - k; --i)
		res *= i;
	for (int i = 1; i <= k; ++i)
		res /= i;

	return res;
}

int bs(int val, vector <int> &ar)
{
	int l = 0, r = ar.size() - 1;
	int res = ar.size();
	while (l <= r)
	{
		int m = (r + l) >> 1;

		if (ar[m] >= val)
		{
			res = m;
			r = m - 1;
		}
		else if (ar[m] < val)
			l = m + 1;
	}

	return res;
}

void task(int X)
{
	int n, m;
	scanf("%d%d", &n, &m);
	vector <vector <int> > ar (n, vector <int> (m));

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &ar[i][j]);

	string res = "YES";

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			int val = ar[i][j];
			bool s1 = 1, s2 = 1;
			for (int k = 0; k < m; ++k)
			{
				if (ar[i][k] > val)
					s1 = 0;
			}

			for (int k = 0; k < n; ++k)
			{
				if (ar[k][j] > val)
					s2 = 0;
			}

			if (!s1 && !s2)
			{
				res = "NO";
				break;
			}
		}
		if (res[0] == 'N')
			break;
	}

	cout << "Case #" << X << ": " << res << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i)
		task(i + 1);

	return 0;
}