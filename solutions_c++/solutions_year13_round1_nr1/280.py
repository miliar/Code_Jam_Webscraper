#include <iostream>
#include <fstream>
//#include <stdio.h>

using namespace std;

long long r, t;
long long bins(long long lo, long long hi)
{
	if (hi == lo)
		return lo;

	long long k = (lo+hi)/2;
	if (k == lo) k++;
	double tmp = 2*r+1;
	tmp = tmp *= k;
	double tmp1 = 2*(k-1);
	tmp1 *= k;
	tmp += tmp1;
	double tt = t;

	if (tmp > tt)
		return bins(lo, k-1);

	long long val = (2*r+1)*k + 2*(k-1)*k;
	if (val <= t)
		return bins(k, hi);
	else
		return bins(lo, k-1);
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	int testnum = 0;
	//scanf("%d", &testnum);
	cin >> testnum;
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		cin >> r >> t;

		long long res = bins(0, t);

		cout << "Case #" << testcase << ": " << res << endl;
		//printf("Case #%d: %d\n", testcase, a+b);
	}

	return 0;
}
