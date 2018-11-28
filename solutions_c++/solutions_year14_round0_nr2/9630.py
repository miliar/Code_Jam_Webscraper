#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define For(i, n) for(int i = 0; i < (n); i++)
#define ForD(i, n) for(int i = (n) - 1; i >= 0; i--)
#define in cin >>
#define out cout <<
#define ft first
#define sd second
typedef long long LL;

double val(int n, double C, double F, double X)
{
	if (n < 0)
		return 1e9;

	double prod = 2;
	double total = 0;
	double res = 0;
	int farmCnt = 0;

	while (farmCnt < n)
	{
		res += C / prod;
		prod += F;
		farmCnt++;
	}

	res += X / prod;
	return res;
}

double Solve(double C, double F, double X)
{
	int beg = 0, end = X + 1;

	while (beg < end - 1)
	{
		int leftThird = (2 * beg + end) / 3;
		int rightThird = (beg + 2 * end) / 3;

		if (val(leftThird, C, F, X) > val(rightThird, C, F, X))
			beg = rightThird;
		else
			end = leftThird;
	}

	double res = 1e9;
	for (int i = -200; i < 200; i++)
		res = min(res, val(i + beg, C, F, X));
	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	in t;
	For (k, t)
	{
		double c, f, x;
		in c >> f >> x;
		printf("Case #%d: %.7lf\n", k + 1, Solve(c, f, x));
	}
}
