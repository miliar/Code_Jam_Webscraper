#include<stdio.h>
int main()
{
	long long t, i;
	long long n, k, j;
	char in[1000],out[2010];
	freopen("inputA.txt", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	scanf("%lld\n", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%s", in);
		n = 0;
		k = j = 1001;
		out[k] = in[n];
		out[k + 1] = 0;
		n++;

		while (in[n] > 'A' - 1 && 'Z' + 1 > in[n])
		{
			if (in[n] >= out[k])
			{
				out[k - 1] = in[n];
				k--;
			}
			else
			{
				out[j + 1] = in[n];
				j++;
			}
			n++;
		}
		out[j + 1] = 0;
		printf("case #%lld: %s\n", i+1, &out[k], 1000);
	}
	return 0;
}