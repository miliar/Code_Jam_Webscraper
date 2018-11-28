#include <stdio.h>

int main()
{
	FILE *inputf, *output;
	int cases, nocase, input, digitCount, digitarray[10];
	inputf = fopen("A-large.in.txt", "r");
	output = fopen("A-large.out.txt", "w");
	fscanf(inputf, "%d", &nocase);
	//scanf("%d", &nocase);

	for (int counter = 1; counter <= nocase; counter++)
	{
		for (int i = 0; i < 10; i++)
			digitarray[i] = 0;
		digitCount = 0;
		fscanf(inputf, "%d", &input);
		//scanf("%d", &input);
		if (input == 0)
		{
			fprintf(output, "Case #%d: INSOMNIA\n", counter);
			//printf("Case #%d: INSOMNIA\n", counter);
			continue;
		}
		int value, rem, res;
		for (int i = 1; digitCount != 10; i++)
		{
			res = value = input * i;
			while (value)
			{
				rem = value % 10;
				value = value / 10;
				if (digitarray[rem] == 0)
				{
					digitarray[rem]++;
					digitCount++;
				}
			}
		}
		fprintf(output, "Case #%d: %d\n", counter, res);
		//printf("Case #%d: %d\n", counter, res);
	}
	fclose(inputf);
	fclose(output);
}