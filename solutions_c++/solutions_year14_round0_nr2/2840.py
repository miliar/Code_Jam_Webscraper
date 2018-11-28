#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		
		double rate = 2.0;
		double time = 0;
		while (true)
		{
			double wait = C / rate + X / (F + rate);
			double direct = X / rate;
			if (wait < direct)
			{
				time += C / rate;
				rate += F;
			} else {
				time += direct;
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n", t, time);
	}
	return 0;
}
