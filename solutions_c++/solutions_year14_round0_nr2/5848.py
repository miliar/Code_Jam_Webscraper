#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int test;
	double c, f, x;
	double res, r, maxt;
	double secm, thim;
	cin >> test;
	for(int i=0; i<test; i++)
	{
		res = 0.00000000;
		r = 2.00000000;
		scanf("%lf %lf %lf", &c, &f, &x);
		while(x/r > (x/(r+f) + c/r))
		{
			res += c/r;
			r += f;
		}
		res += x/r;
		printf("Case #%d: %.7lf\n", i+1, res);
	}
}
