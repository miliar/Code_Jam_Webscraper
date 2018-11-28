#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, caseno = 1;
	double c, f, x, res, rate;
	cin >> t;
	while(t--)
	{
		res = 0.0;
		cin >> c >> f >> x;
		rate = 2;
		while(1)
		{
			if((c/rate)+(x/(rate+f)) < x/rate)
			{
				res += c/rate;
				rate += f;
			}
			else
			{
				res += x/rate;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", caseno, res);
		caseno++;
	}
	return 0;
}