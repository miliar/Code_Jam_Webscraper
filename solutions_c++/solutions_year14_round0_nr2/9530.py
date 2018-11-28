#include <stdio.h>

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double production = 2.0;
		double timenobuy = 0;
		double totaltime = 0;
		double time = 0;
		double timetobuyfarm = 0;
		do
		{
			totaltime += timetobuyfarm;
			timetobuyfarm = C / production;
			timenobuy = X / production;
			production += F;
			double timeafterbuy = X / production;
			time = timetobuyfarm + timeafterbuy;			
		} while (time < timenobuy);
		totaltime += timenobuy;
		printf("Case #%d: %lf\n", i+1, totaltime);
	}
	getchar();
}