#include "stdio.h"

FILE *inputFile;
FILE *outputFile;

int main(int argc, char* argv[])
{
	inputFile = fopen("input.txt", "r");
	outputFile = fopen("output.txt", "w");

	if(!(inputFile && outputFile))
	{
		fprintf(outputFile, "unable to open io files");
		return -1;
	}

	//read test case count
	int T;
	fscanf(inputFile, "%d", &T);

	for (int Ti = 1; Ti <= T; ++Ti) 
	{
		unsigned long long t=0, r=0;
		unsigned long long c=0;
		fscanf(inputFile, "%llu%llu", &r, &t);
		while(1)
		{
			unsigned long long ri = ((r+1)*(r+1)) - (r*r);
			if(t >= ri)
			{
				c++;
				t -= ri;
				r += 2;
			}
			else 
				break;
		}

		fprintf(outputFile, "Case #%d: %llu\n", Ti, c);
	}
	
	fclose(inputFile);
	fclose(outputFile);
	return 0;
}


