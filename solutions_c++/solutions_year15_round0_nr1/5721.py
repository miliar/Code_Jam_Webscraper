#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 1002

int minimum_friends(int Smax, char shyness[])
{
	int minf = 0;
	int curr_shyness = 0;

	for (int i = 0; i <= Smax; i++)
	{
		if (curr_shyness >= i) curr_shyness += shyness[i] - '0';
		else
		{
			if (shyness[i] > '0')
			{
				minf += i - curr_shyness;
				curr_shyness = i + (shyness[i] - '0');
			}
		}
	}

	return minf;
}

int main()
{
	int n, cases;
	FILE *fin, *fout;

	fin = fopen("A-large.in", "r");
	fout = fopen("out.txt", "w");

	fscanf(fin, "%d", &n);
	cases = 1;

	///////////// Code begins here /////////////////////
	int smax;
	char shyness[MAXN];

	while (n--)
	{
		fscanf(fin, "%d %s", &smax, shyness);
		fprintf(fout, "Case #%d: %d\n", cases++, minimum_friends(smax, shyness));
	}

	///////////// Code ends here /////////////////////

	fclose(fin);
	fclose(fout);
	
	return 0;
}
