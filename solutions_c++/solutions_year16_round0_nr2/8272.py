#include<cstdio>
#include<cstring>
#include<cstdlib>
char arr[101];
int main(void)
{
	FILE* input;
	FILE* output;
	input = fopen("B-large.in", "r");
	output = fopen("output.txt", "w");
	int tc;
	fscanf(input,"%d", &tc);
	for (int q = 1; q <= tc; q++)
	{
		fscanf(input, "%s", arr);
		int len = strlen(arr),cnt=0;
		char tmp = arr[0];
		for (int i = 1; i < len; i++)
		{
			if (tmp != arr[i])
			{
				cnt++;
				tmp = arr[i];
			}
		}
		if (tmp == '-')
			cnt++;
		fprintf(output, "Case #%d: %d\n", q, cnt);
	}

	fclose(input);
	fclose(output);
	return 0;
}