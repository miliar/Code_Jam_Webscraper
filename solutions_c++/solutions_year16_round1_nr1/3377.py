#include <stdio.h>
#include <string>


int main()
{
	FILE *inputf, *output;
	int cases, nocase, input, digitCount;
	char digitarray[1001];
	std::string result;
	inputf = fopen("A-large.in.txt", "r");
	output = fopen("large.txt", "w");
	fscanf(inputf, "%d", &nocase);
	//scanf("%d", &nocase);

	for (int counter = 1; counter <= nocase; counter++)
	{
		fscanf(inputf, "%s", digitarray);
		//scanf("%s", digitarray);
		digitCount = 0;
		int len = strlen(digitarray);
		char last;
		for (int i = 0; i < len; i++)
		{
			char a = toupper(digitarray[i]);
			if (i == 0)
				result = last = a;
			else if (a < result[0])
			{
				last = a;
				result = result + last;
			}
			else
			{
				last = a;
				result = last + result;	
			}
		}
		//printf("Case #%d: %s\n", counter, result.c_str());
		fprintf(output, "Case #%d: %s\n", counter, result.c_str());
	}
	fclose(inputf);
	fclose(output);
}