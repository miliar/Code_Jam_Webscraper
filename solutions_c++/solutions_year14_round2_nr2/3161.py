#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);

	for(int ncase = 1; ncase<=t; ncase++)
	{
		int a, b, k;
		scanf("%d%d%d", &a, &b, &k);
		int count = 0;
		for(int i=0; i<a; i++)
		{
			for(int j=0; j<b; j++)
			{
				int aux = i&j;
				if(aux<k)
					count++;
			}
		}
		printf("Case #%d: %d\n", ncase, count);
	}
}
