#pragma warning(disable:4996)
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>

using namespace std;

const char inFileName[] = "A-large.in";
const char outFileName[] = "A-large.out";

int T, n;
bool digits[10];
int digitsFound;

void setDigits(int num)
{
	while (num > 0)
	{
		int x = num % 10;
		if (!digits[x])
		{
			digits[x] = true;
			digitsFound++;
		}
		num /= 10;
	}
}

int main() {

	FILE* inFile = fopen(inFileName, "r");
	FILE* outFile = fopen(outFileName, "w");

	fscanf(inFile, "%d", &T);
	for (int t = 0; t < T; t++)
	{
		fscanf(inFile, "%d", &n);

		if (n == 0) 
		{
			fprintf(outFile, "Case #%d: INSOMNIA\n", t + 1);
			continue;
		}

		memset(digits, false, sizeof(digits));
		digitsFound = 0;
		int sol = 0;
		while (digitsFound < 10) 
		{
			sol = sol + n;
			setDigits(sol);
		}

		fprintf(outFile, "Case #%d: %d\n", t + 1, sol);
	}

	fclose(inFile);
	fclose(outFile);
	return 0;
}
