#include <iostream>

int solve(int n)
{
	if (n == 0)
		return -1;
	int ninit = n;
	bool flags[10];
	flags[0] = flags[1] = flags[2] = flags[3] = flags[4] = flags[5] = flags[6] = flags[7] = flags[8] = flags[9] = false; 
	int iter = 1;
	for (; iter < 1000; iter++)
	{
		n = ninit * iter;
		int temp = n;
		while (temp > 0)
		{
			flags[temp % 10] = true;
			temp /= 10;
		}
		if (flags[0] && flags[1] && flags[2] && flags[3] && flags[4] && flags[5] && flags[6] && flags[7] && flags[8] && flags[9])
			break;
	}
	if (iter == 1000)
		return -1;
	return n;
}

void main()
{
	printf("Hello world!\n");
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");
	int n = 0;
	fscanf(fin, "%d", &n);
	for (int i = 0; i < n; ++i)
	{
		int num = 0;
		fscanf(fin, "%d", &num);
		int s = solve(num);
		if (s < 0)
		{
			printf("INSOMNIA\n");
			fprintf(fout, "CASE #%d: INSOMNIA\n", i + 1);
		}
		else
		{
			printf("%d\n", s);
			fprintf(fout, "CASE #%d: %d\n", i + 1, s);
		}
	}
	fclose(fin);
	fclose(fout);
}