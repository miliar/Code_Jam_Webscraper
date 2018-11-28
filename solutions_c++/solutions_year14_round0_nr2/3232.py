#include <cstdio>
#include <cmath>
using namespace std;
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int p = 0; p < t; ++p)
	{
		double c, f, x;
		scanf ("%lf%lf%lf", &c, &f, &x);
		double a = 0.0, r = 2.0, ans = 0.0;
		while (fabs(a-x) > 0.000001)
		{
			if (x/r <= (c/r) + (x/(r+f)))
			{
				a = a + (x/r);
				ans += (x/r);
				break;
			}	
			else
			{	
				a = (c / r);
				ans += (c/r);
				r += f;
				a = 0.0;
			}	
		}
		printf ("Case #%d: %.7f\n", p+1, ans);
	}	
	return 0;
}