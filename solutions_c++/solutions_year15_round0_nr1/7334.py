#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>

int main()
{
	FILE *filein, *fileout;
	filein = fopen("A-large.in", "r");
	fileout = fopen("out_standing_ovation_large.txt", "w");

	int testcaseamount, totalstanding, addedfriends, shynessmax;
	char shynessi;
	fscanf(filein, "%d", &testcaseamount);
	for (int k = 1; k <= testcaseamount; k++)
	{
		fscanf(filein, "%d", &shynessmax);
		totalstanding = 0;
		addedfriends = 0;
		for (int i = 0; i <= shynessmax; i++)
		{
			if (fscanf(filein, " %c", &shynessi) && shynessi != '0')
			{
				//there are people at shynessi
				shynessi -= '0';
				if (totalstanding < i)
				{
					addedfriends += i - totalstanding;
					totalstanding += i - totalstanding;
				}
				totalstanding += shynessi;
			}
		}

		fprintf(fileout, "Case #%d: %d\n", k, addedfriends);

	}
	return 0;
}