#include "stdio.h"
#include <iostream>


int main()
{
	using namespace std;
	FILE * finp;
	FILE * foutp;

	int t;
	char c[101];
	finp = fopen("1.in", "r");
	foutp = fopen("1.out", "w");

	fscanf(finp, "%d", &t);

	for (int i = 0; i<t; ++i)
	{
		int rs = 0;
		char last;
		fscanf(finp, "%s", c);
		for (int j = 0;c[j] != '\0';++j)
		{
			last = c[j];
			if (j == 0)continue;
			if (c[j] != c[j-1])++rs;
		}
		if (last == '-')++rs;

		fprintf(foutp, "Case #%d: %d\n", i + 1, rs);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
