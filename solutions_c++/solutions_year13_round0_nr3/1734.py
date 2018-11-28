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

bool is_pali(int64 v)
{
	int64 t1 = v;
	int64 t2 = 0;
	while (v)
	{
		t2 = t2 * 10 + v % 10;
		v /= 10;
	}

	return t1 == t2;
}

vector <int64> p_ar;

void prec()
{
	for (int64 i = 1; i * i <= 100000000000000; ++i)
	{
		if (!is_pali(i))
			continue;

		int64 isqr = i * i;

		if (is_pali(isqr))		
			p_ar.push_back(isqr);
	}

	//cerr << p_ar.size() << endl;
}

void task(int X)
{
	int64 a, b;
	int64 res = 0;

	cin >> a >> b;
	
	for (int i = 0; i < p_ar.size(); ++i)
		if (p_ar[i] >= a && p_ar[i] <= b)
			++res;

	cout << "Case #" << X << ": " << res << endl;
}

int main()
{
	freopen("C-large-1.in", "r", stdin);
	freopen("C-large-1.out", "w", stdout);

	int t;
	cin >> t;

	prec();

	for (int i = 0; i < t; ++i)
		task(i + 1);

	return 0;
}