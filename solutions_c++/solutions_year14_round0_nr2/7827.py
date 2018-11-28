#include <stdio.h>
int main()
{
	double farmCost, plusCookie, goal, time;
	double currGetCookie = 2;
	int totalTestCase;
	FILE* input = fopen("B-large.in", "r");
	FILE* output = fopen("output.out", "w");
	time = 0;
	fscanf(input, "%d", &totalTestCase);

	for (int testcase = 1; testcase <= totalTestCase; testcase++)
	{
		fscanf(input, "%lf %lf %lf", &farmCost, &plusCookie, &goal);
		while (1)
		{
			if ((goal / currGetCookie)> (farmCost / currGetCookie) + (goal / (currGetCookie + plusCookie)))
			{

				time += farmCost / currGetCookie;
				currGetCookie += plusCookie;
			}

			else
			{
				time += (goal / currGetCookie);
				break;
			}
		}

		fprintf(output, "Case #%d: %.7lf\n", testcase, time);
		time = 0;
		currGetCookie = 2;
	}


	fclose(input);
	fclose(output);
	return 0;
}