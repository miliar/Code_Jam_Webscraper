#include <cstdio>
#include <cmath>
using namespace std;

double f(double r0, double n)
{
	return n * (2*r0 + 2*n - 1);
}

long long calc(double r0, double t)
{
	double right = 2000000000,
		      left = 0,
			  med = 0;

	while (right - left > 1)
	{
		med = (right + left) / 2;
		if ( f(r0, med) < t)
		{
			left = med;
		}
		else
			right = med;
	}
	long long l = (long long) left;

	if ( f(r0, l) <= t && f(r0, l + 1) > t)
		return (long long) l;
	l = l + 1;
	if ( f(r0, l) <= t && f(r0, l + 1) > t)
		return (long long) l;
	l = l + 1;
	if ( f(r0, l) <= t && f(r0, l + 1) > t)
		return (long long) l;
	l = l - 3;
	if ( f(r0, l) <= t && f(r0, l + 1) > t)
		return (long long) l;

	return 0;
}

long long calc2(double r0, double t)
{
	double res = ( sqrt(4*r0*r0 - 4*r0 + 1 + 8*t) - (2*r0 - 1) ) / 4;
	return (long long) (res);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int num;
	long long res;
	double r0, t;
	scanf("%d", &num);
	for (int k = 1; k <= num; k++)
	{
		printf("Case #%d: ", k);
		scanf("%lf %lf", &r0, &t);
		res = calc(r0, t);
		printf("%lld \n", res);
	}

	return 0;
}