#include "stdio.h"
#include <iostream>


int main()
{
	using namespace std;
	FILE * finp;
	FILE * foutp;

	int t;
	int a[10];
	finp = fopen("1.in", "r");
	foutp = fopen("1.out", "w");

	fscanf(finp, "%d", &t);

	for (int i = 0; i<t; ++i)
	{
		long int n,nn;
		long int rs = 0;
		bool t = true;
		long int c = 0;
		fscanf(finp, "%d", &n);
		if (n == 0)
		{
			fprintf(foutp, "Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		for (int j = 0;j < 10;++j)
		{
			a[j] = 0;
		}
		while (++c)
		{
			nn = c*n;
			++rs;
			while (nn)
			{
				a[nn % 10] = 1;
				nn /= 10;
			}
			t = true;
			for (int j = 0;j < 10;++j)
			{
				t = t && (a[j] == 1);
				if (t == false)break;
			}
			if (t == true)
			{
				break;
			}
		}
		fprintf(foutp, "Case #%d: %d\n", i + 1, rs*n);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
