#include <stdio.h>
#include <stdint.h>

int main()
{
	unsigned int caseTotal;
	fscanf(stdin, "%u\n", &caseTotal);

	for (unsigned int caseNum = 0; caseNum < caseTotal; ++caseNum)
	{
		double c, f, x;
		fscanf(stdin, "%lf %lf %lf\n", &c, &f, &x);

		double result = 0.0;
		double s = 2.0;

		for (;;)
		{
			double left = x/s;
			double right = c/s + x/(s+f);

			if (left >= right)
			{
				result+=(c/s);
				s+=f;
			}
			else
			{
				result+=(x/s);
				break;
			}
		}

PRINT:
		printf("Case #%u: %.7f\n", caseNum+1, result);
	}

	return 0;
}
