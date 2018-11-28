// ProblemA.cpp : Defines the entry point for the console application.
//

#include <stdio.h>


int main()
{
	long long int T;
	long long int N;
	long long int P;
	long long int tempP;
	int digitsSeen = 0;
	int digitsMap[10];


	scanf("%lld", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%lld", &N);

		//reset temp variables
		digitsSeen = 0;
		for (int k = 0; k < 10; k++)
		{
			digitsMap[k] = 0;
		}

		if (N > 0)
		{
			for (int j = 1; ; j++)
			{
				P = N * j;
				tempP = P;
				while (tempP)
				{
					int digit = tempP % 10;
					tempP /= 10;
					if (digitsMap[digit] == 0)
					{
						++digitsMap[digit];
						++digitsSeen;
					}
					if (digitsSeen == 10)
						break;
				}
				if (digitsSeen == 10)
					break;
			}
		}

		if (digitsSeen == 10)
			printf("Case #%d: %lld\n", i+1, P);
		else
			printf("Case #%d: INSOMNIA\n", i+1);
	}
    return 0;
}

