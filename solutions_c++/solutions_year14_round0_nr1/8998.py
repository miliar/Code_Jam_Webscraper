#include <stdio.h>
#include <stdint.h>

int main()
{
	unsigned int caseTotal;
	fscanf(stdin, "%u\n", &caseTotal);

	for (unsigned int caseNum = 0; caseNum < caseTotal; ++caseNum)
	{
		unsigned int row0;
		fscanf(stdin, "%u\n", &row0);

		unsigned int card0[4][4];
		for (unsigned int ii = 0; ii < 4; ++ii)
		{
			for (unsigned int jj = 0; jj < 4; ++jj)
			{
				fscanf(stdin, "%u", &card0[ii][jj]);
			}
		}

		unsigned int row1;
		fscanf(stdin, "%u\n", &row1);

		unsigned int card1[4][4];
		for (unsigned int ii = 0; ii < 4; ++ii)
		{
			for (unsigned int jj = 0; jj < 4; ++jj)
			{
				fscanf(stdin, "%u", &card1[ii][jj]);
			}
		}

		unsigned int result = 0;
		unsigned int number = 0;

		unsigned int* c0 = card0[row0-1];
		unsigned int* c1 = card1[row1-1];

		bool foundSomething = false;
		for (unsigned int ii = 0; ii < 4; ++ii)
		{
			unsigned int first = c0[ii];
			for (unsigned int jj = 0; jj < 4; ++jj)
			{
				unsigned int second = c1[jj];
				if (first == second)
				{
					foundSomething = true;
					if (0 == number)
					{
						number = first;
					}
					else
					{
						result = 1;
						goto PRINT;
					}
				}
			}
		}

		if (!foundSomething)
		{
			result = 2;
		}

PRINT:
		switch (result)
		{
		case 0:
			{
				printf("Case #%u: %u\n", caseNum+1, number);
			}
		break;

		case 1:
			{
				printf("Case #%u: Bad magician!\n", caseNum+1);
			}
		break;

		case 2:
			{
				printf("Case #%u: Volunteer cheated!\n", caseNum+1);
			}
		break;
		};

	}

	return 0;
}
