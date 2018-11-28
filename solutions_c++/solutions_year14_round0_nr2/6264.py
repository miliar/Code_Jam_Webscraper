#include <iostream>
#include <stdio.h>
using namespace std;

using namespace std;

int main()
{
	int cases = 0, counter = 0;
	double result[100];
	double input[3], upperC = 10000.0, upperF = 100.0, upperX = 100000.0;
	bool incomplete = false;

	errno_t err;

	FILE* hfile;
	err = fopen_s(&hfile, "input.txt", "rb");

	if (err == 0)
	{
		printf("The file 'input.txt' was opened\n");
	}
	else
	{
		printf("The file 'input.txt' was not opened\n");
		exit(15);
	}

	while (cases < 1 || cases > 100)
	{
		fscanf_s(hfile, "%d", &cases);
	}

	while (counter < cases)
	{
		incomplete = true;
		while (incomplete)
		{
			incomplete = false;

			for (int i = 0; i < 3; i++)
			{
				input[i] = 0;
			}

			fscanf_s(hfile, "%lf %lf %lf", &input[0], &input[1], &input[2]);

			if (input[0] < 1.0 || input[0] > upperC)
				incomplete = true;			
			if (input[1] < 1.0 || input[1] > upperF)
				incomplete = true;
			if (input[2] < 1.0 || input[2] > upperX)
				incomplete = true;
		}

		double shortest = 0.0, rate = 2.0;
		incomplete = true;

		//0: Cookies per farm, 1: Increase per farm, 2: target
		while (incomplete)
		{
			if (input[0] / rate + input[2] / (rate + input[1]) < input[2] / rate)
			{
				shortest += input[0] / rate;
				rate += input[1];
			}
			else
			{
				shortest += input[2] / rate;
				incomplete = false;
			}
		}

		result[counter] = shortest;
		counter += 1;
	}

	fclose(hfile);

	fopen_s(&hfile, "output.txt", "wb");
	for (int i = 0; i < cases; i++)
	{
		fprintf(hfile, "Case #%d: %lf\n", i + 1, result[i]);
	}
	
	return 0;
}