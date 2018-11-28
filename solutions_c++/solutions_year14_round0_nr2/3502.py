#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

#define eps 1e-7

int main()
{
	int csnum;
	double c, f, x;
	//freopen ("1.in", "r", stdin);
	//freopen ("b.out", "w", stdout);
	//freopen ("B-small-attempt3.in", "r", stdin);
	freopen ("B-large.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	
	scanf ("%d", &csnum);
	for (int cs = 1; cs <= csnum; cs++)
	{
		scanf ("%lf %lf %lf", &c, &f, &x);

		double ans = x / 2.0;
		double t0 = 0;
		double v = 2.0;
		double t = 0;
		for (; x / v > c / v + x / (v + f); )
		{
			//printf ("v=%lf t0=%lf c/v=%lf t=%lf x/v=%lf ans=%lf\n", v, t0, c/v, t, x/v, ans);
			t0 += c / v;
			v += f;
			t = t0 + x / v;
			ans = min(ans, t);
			//printf (" v=%lf t0=%lf t=%lf ans=%lf\n", v, t0, t, ans);

		}
		printf ("Case #%d: %.7lf\n", cs, ans);
	}

	return 0;
}

