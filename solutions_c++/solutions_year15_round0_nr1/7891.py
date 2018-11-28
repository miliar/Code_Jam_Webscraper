#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	FILE *in;
	FILE* out;
	in = fopen("A-large.in", "r");
	out = fopen("A-large.out", "w+");
	int T;
	fscanf(in, "%d", &T);
	int Smax;
	char shyness[2000];
	int x;
	int result;
	for(int i = 0; i < T; i++)
	{
		x = 0;
		result = 0;
		fscanf(in, "%d %s", &Smax, &shyness);
		x = shyness[0] - '0';
		for (int j = 1; j <= Smax; j++)
		{
			if (x < j && shyness[j] != '0')
			{
				result += (j - x);
				x = j;
			}
			x += (shyness[j] - '0');
		}
		fprintf(out, "Case #%d: %d\n", (i + 1),result);
	}
	return 0;
}