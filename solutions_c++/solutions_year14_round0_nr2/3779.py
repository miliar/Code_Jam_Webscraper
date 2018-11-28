#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int t, i, j, k;
	double c, f, x, rate, ans, nofarm, farm;
	scanf("%d", &t);
	for(i=1; i<=t; i++)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		rate=2;
		if(x/rate<c/rate+x/(rate+f)) printf("Case #%d: %.7lf\n", i, x/rate);
		else
		{
			ans=c/rate;
			rate+=f;
			while(x/rate>c/rate+x/(rate+f))
			{
				ans+=c/rate;
				rate+=f;
			}
			printf("Case #%d: %.7lf\n", i, ans+x/rate);
		}
	}

	return 0;
}
