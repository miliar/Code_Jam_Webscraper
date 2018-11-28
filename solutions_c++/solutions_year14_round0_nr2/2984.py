#include <stdio.h>

int main(void)
{
	int casis;
	double c, f, x;
	double total;
	double spow;
	double result;
	double temp;
	int i, j, k;

	freopen("B-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);

	scanf("%d", &casis);

	for(i = 0; i < casis; i++)
	{
		//scan
		scanf("%lf %lf %lf", &c, &f, &x);
		result = x / 2;

		//calc
		for(j = 0; j <= x / c + 1; j++)
		{
			temp = 0;
			temp += x / (2 + f * j);

			for(k = 0; k < j; k++)
				temp += c / (2 + f * k);
			
			if(temp < result)
				result = temp;

		}

		printf("Case #%d: %.8lf\n", i + 1, result);
	}

}