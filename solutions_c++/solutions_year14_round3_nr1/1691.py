#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int t, p, q;
FILE *inputFile, *outputFile;
double temp;
bool isEnd;

int main(int argc,char *argv[])
{
	inputFile = fopen(argv[1], "r");
	outputFile = fopen(argv[2], "w");

	fscanf(inputFile, "%d", &t);

	for (int iii = 0; iii < t; iii++)
	{
		fscanf(inputFile, "%d/%d", &p, &q);

		double r = ((double)p) / q;
		unsigned long oszto = 1;

		isEnd = false;
		for (int i = 1; i < 41; i++)
		{
			oszto *= 2;
			double e = r / (((double)1) / oszto);

			// printf("p=%d q=%d r=%lf oszto=%lu e=%lf\n", p, q, r, oszto, e);

			if (modf(e, &temp) == 0)
			{
				unsigned long szorzo = 1;
				int szamolo = -1;
				while (szorzo < e)
				{
					szorzo *= 2;
					szamolo++;
				}

				fprintf(outputFile, "Case #%d: %d\n", iii + 1, (szamolo>0) ? i - szamolo : i);
				isEnd = true;
				break;
			}
		}

		if (!isEnd)
			fprintf(outputFile, "Case #%d: impossible\n", iii + 1);

		// fprintf(outputFile, "Case #%d: %lu\n", iii + 1, counter % 1000000007);
	}

	fclose(inputFile);
	fclose(outputFile);

	// double a, b, c, d, e;
	// double temp;
	// a = 1;
	// // b = 256;
	// b = 1099511627776;

	// // 549755813888
 //   // 1099511627776

	// c = 123;
	// d = 31488;

	// e = (c/d) / (a/b);

	// if (modf(e, &temp) == 0)
	// // if (true)
	// {
	// 	printf("TRUE\n");
	// }
	// else
	// {
	// 	printf("FALSE\n");
	// }
}