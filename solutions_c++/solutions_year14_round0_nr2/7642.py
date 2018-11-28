#include <cstdio>
using namespace std;

int main()
{
	int T;
	double C, F, X;

	scanf("%d", &T);

	for(int tCase = 1; tCase <= T; tCase++)
	{
		scanf("%lf %lf %lf", &C, &F, &X);

		double r = 2;
		double tr = 0;
		double tx = X / r;
		double tt = tr + tx;

		while(true)
		{
			tr += C / r;
			r += F;
			tx = X / r;

			if(tr + tx > tt)
				break;

			tt = tr + tx;
		}

		printf("Case #%d: %.7lf\n", tCase, tt);
	}

	return 0;
}