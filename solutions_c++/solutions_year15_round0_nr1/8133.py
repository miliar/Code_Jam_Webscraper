#include <stdio.h>

FILE *fs = fopen("A-large.in", "r");
FILE *fp = fopen("output.txt", "w");

int main()
{
	long long T;

	fscanf(fs,"%lld", &T);

	for (long long tmp = 1; tmp <= T; tmp++)
	{
		long long max, shy[1005], count=0, friends=0;
		char input[1005];

		fscanf(fs,"%lld %s", &max, input);
		for (long long i = 0; i <= max; i++)
		{
			shy[i] = input[i] - '0';
			while (count < i)
			{
				count++;
				friends++;
			}
			count += shy[i];
		}
		fprintf(fp,"Case #%lld: %lld\n", tmp, friends);
	}

	return 0;
}