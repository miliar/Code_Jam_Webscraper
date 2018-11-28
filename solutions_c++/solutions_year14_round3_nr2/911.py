#include <stdio.h>
#include <iostream>
#include <cstdlib>

using namespace std;

int t, n;
FILE *inputFile, *outputFile;
char strings[10][150];
bool used[10];
unsigned long counter;
int result[10];
bool usedCharacter[123];

bool checkResult()
{
	for (int i = 97; i < 123; i++)
	{
		usedCharacter[i] = false;
	}

	int j;
	char lastCharacter = 0;
	for (int i = 0; i < n; i++)
	{
		j = 0;

		while (strings[result[i]][j] != 0)
		{
			if (strings[result[i]][j] != lastCharacter)
			{
				lastCharacter = strings[result[i]][j];

				if (usedCharacter[lastCharacter] == false)
				{
					usedCharacter[lastCharacter] = true;
				}
				else
				{
					return false;
				}
			}

			j++;
		}
	}

	return true;
}

void solve(int step)
{
	for (int i = 0; i < n; i++)
	{
		if (!used[i])
		{
			result[step] = i;
			used[i] = true;

			if (step == n-1)
			{
				if (checkResult())
				{
					counter++;
				}
			}
			else
			{
				solve(step+1);
			}

			used[i] = false;
		}
	}
}

int main(int argc,char *argv[])
{
	inputFile = fopen(argv[1], "r");
	outputFile = fopen(argv[2], "w");

	fscanf(inputFile, "%d", &t);

	for (int iii = 0; iii < t; iii++)
	{
		counter = 0;

		fscanf(inputFile, "%d", &n);

		for (int i = 0; i < n; i++)
		{
			fscanf(inputFile, "%s", strings[i]);

			used[i] = false;
		}

		solve(0);

		fprintf(outputFile, "Case #%d: %lu\n", iii + 1, counter % 1000000007);
	}

	fclose(inputFile);
	fclose(outputFile);
}