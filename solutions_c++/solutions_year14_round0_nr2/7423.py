#include<stdio.h>
#include<stdlib.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int turn = 1; turn <= T; turn++)
	{
		// C = farm cost
		// F = cookie rate boost
		// X = required cookies
		long float C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		long float time = 0.0;
		long float cookieRate = 2.0;
		long float farmCount = 0.0;

		while((X / cookieRate) > ((C / cookieRate) + (X / (cookieRate + F))))
		{
			time += C / cookieRate;
			cookieRate += F;
		}
		time += X / cookieRate;

		printf("Case #%d: %.7llf\n", turn, time);
	}

	fflush(stdin);
	getchar();
	return 0;
}