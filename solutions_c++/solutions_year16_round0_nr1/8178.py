#include<cstdio>
#include<cstring>
#include<cstdlib>
bool chk[10];
int main(void)
{
	FILE* input;
	FILE* output;
	input = fopen("A-large.in", "r");
	output = fopen("output.txt", "w");
	int tc;
	fscanf(input,"%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		memset(chk, false, sizeof(chk));
		int n;
		int cnt = 0;
		fscanf(input,"%d", &n);
		if (n == 0)
			fprintf(output,"Case #%d: INSOMNIA\n", i);
		else
		{
			for (int k = 1;; k++)
			{
				long long tmp = k*n;
				while (tmp != 0)
				{
					if (!chk[tmp % 10])
					{
						cnt++;
						chk[tmp % 10] = true;
					}
					tmp /= 10;
				}
				if (cnt == 10)
				{
					fprintf(output,"Case #%d: %lld\n", i, k*n);
					break;
				}
			}

		}
	}

	fclose(input);
	fclose(output);
	return 0;
}