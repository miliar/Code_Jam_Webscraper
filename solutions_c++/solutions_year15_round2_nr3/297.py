#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

#define int64 long long
int64 s[100], l[100];

const int EPS = 1e-8;

bool eq(double a, double b)
{
	return abs(a - b) < EPS;
}
bool ls(double a, double b)
{
	return !eq(a, b) && a < b;
}

void Solution()
{
	int n;
	cin >> n;
	int m = 0;

	for (int i = 0; i < n; i++)
	{
		int64 pos0, cnt, l0;
		cin >> pos0 >> cnt >> l0;
		for (int j = 0; j < cnt; j++)
		{
			s[m] = pos0;
			l[m] = l0 + j;
			m++;
		}
	}
	n = m;

	if (n == 1 || l[0] == l[1])
	{
		cout << 0;
		return;
	}

	if (s[0] > s[1])
	{
		swap(s[0], s[1]);
		swap(l[0], l[1]);
	}

	double v = 360.0 / l[0];
	double u = 360.0 / l[1];
	
	if (v > u)
	{
		double w = v - u;
		double rem = (s[1] - s[0]);
		double cross = rem / w;
		double x = cross * v + s[0];
		if (ls(x, 360))
		{
			s[0] = s[1] = x;
			swap(v, u);
			swap(l[0], l[1]);
		}
		else
		{
			cout << 0;
			return;
		}
	}


	//if (v < u)
	{
		double w = u - v;
		double rem = 360 - (s[1] - s[0]);
		if (rem == 0)
			rem = 360;
		double t = rem / w;
		double finLast = max((360 - s[0]) / v, (360 - s[1]) / u);
		if (ls(finLast, t))
			cout << 0;
		else
			cout << 1;
		return;
	}
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}