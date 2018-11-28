#include <stdio.h>
#include <string>


int main()
{
	FILE *inputf, *output;
	int cases, nocase, input, digitCount;
	char digitarray[101];
	inputf = fopen("B-large.in.txt", "r");
	output = fopen("B-large.out.txt", "w");
	fscanf(inputf, "%d", &nocase);
	//scanf("%d", &nocase);

	for (int counter = 1; counter <= nocase; counter++)
	{
		fscanf(inputf, "%s", digitarray);
		//scanf("%s", digitarray);
		digitCount = 0;
		for (int i = strlen(digitarray); i >= 0; i--)
		{
			if (digitarray[i] == '-')
			{
				digitCount++;
				for (int j = 0; j < i; j++)
				{
					if (digitarray[j] == '-')
						digitarray[j] = '+';
					else
						digitarray[j] = '-';
				}
			}
		}
		//printf("Case #%d: %d\n", counter, digitCount);
		fprintf(output, "Case #%d: %d\n", counter, digitCount);
	}
	fclose(inputf);
	fclose(output);
}