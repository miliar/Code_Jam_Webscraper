#include <stdio.h>
#include <string.h>

int main()
{
	FILE *fs = fopen("input.txt", "r");
	FILE *fp = fopen("output.txt", "w");

	int testcase;
	fscanf(fs,"%d", &testcase);

	for (int t = 0; t < testcase; t++)
	{
		int n,rl,sum=0,cnt=0;
		char arr[2000] = { 0, };

		fscanf(fs,"%d ", &n);
		fscanf(fs, "%s", arr);

		rl = strlen(arr);

		for (int j = 0; j <=n; j++)
		{
			int num = arr[j] - '0';

			if (sum < j)
			{
				cnt += (j - sum);
				sum = j;
			}

			sum += num;
		}

		fprintf(fp, "Case #%d: %d\n", t + 1, cnt);
	}

	fclose(fs);
	fclose(fp);
	return 0;
}