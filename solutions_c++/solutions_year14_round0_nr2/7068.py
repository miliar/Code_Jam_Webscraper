#include <stdio.h>
#include <stdlib.h>

int
main()
{
	int nbTests;
	scanf("%d", &nbTests);
	for(int test = 1; test <= nbTests; test++)
	{
		printf("Case #%d: ",test);

		double C;
		double F;
		double X;
		scanf("%lf%lf%lf", &C, &F, &X);

		double tempsMin = 2000000.;
		double curTemps = X / 2.;

		int nbFBuilt = 0;
		while(curTemps < tempsMin)
		{
			tempsMin = curTemps;
			curTemps = curTemps - X / (2 + nbFBuilt*F) + X / (2 + (nbFBuilt+1)*F) + C / (2 + nbFBuilt*F);
			nbFBuilt++;
		}
		printf("%lf\n", tempsMin);
	}


	return 0;
}
