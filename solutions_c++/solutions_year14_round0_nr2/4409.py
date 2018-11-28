#include<cstdio>
using namespace std;

#define MAX 100000

int t;
double c, f, x, t0, t1, sum[MAX];

int main()
{
	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf("%lf %lf %lf", &c, &f, &x);
		
		t0  = x/2.0;
		sum[0] = 0;
		for(int i=1; ; ++i)
		{
			sum[i] = sum[i-1] + c/(2.0 + (i-1)*f);

			t1 = sum[i] + x/(2 + i*f);

			if(t1 > t0) break;
			t0 = t1;
		}

		printf("Case #%d: %.7lf\n", tc, t0);
	}

	return 0;
}
