#include <iostream>
#include <cmath>
using namespace std;
double pi = acos (-1.0);
double sc (double r)
{
	return pi * r * r;
}
int main()
{
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("A-small-output.txt","w",stdout);
	int n;
	cin >> n;
	double t,r;
	double sq = sc (1.0);
	for (int i = 0; i < n; i++)
	{
		cin >> r >> t;
		int ans = 0;
		for (; ;)
		{
			double p = sc (r);
			double q = sc (r + 1);
			double cnt = (q - p) / sq;
			if (cnt < t || fabs(cnt - t) < 1e-9)
			{
				t -= cnt;
				ans++;
			}
			else
				break;
			r += 2;
		}
		printf ("Case #%d: %d\n",i + 1,ans);
	}

	return 0;
}