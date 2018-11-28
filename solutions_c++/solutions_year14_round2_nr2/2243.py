#include <stdio.h>
#include <stdlib.h>
int main()
{
	long int a, b, k, t;
	long int result;
	long int i, j, l;
	long int tmp;
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%d %d %d", &a, &b, &k);
		//пусть a > b
		if (a < b)
		{
			tmp = a;
			a = b;
			b = tmp;
		}
		result = a + b - 1;
		for (j = 1; j < a; j++)
			for (l = 1; l < b; l++)
			{
				if ((j & l) < k)
					result++;
			}
		printf("Case #%d: %d\n", i+1, result);
	}
	return 0;
}