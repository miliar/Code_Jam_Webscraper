#include <stdio.h>
int main()
{
	int N;
	int i;
	int j,k;
	int smax;
	char s[1002];
	int len;
	int r;
	int sum;

	scanf("%d",&N);

	for (i=0;i<N;i++)
	{
		r = 0; sum = 0;
		scanf("%d ",&smax);
		gets(s);
		for (k=0;k<smax+1;k++)
		{
			if (sum<k)
			{
				r += (k - sum);
				sum += (k - sum);
			}
			sum += (s[k]-'0');
		}

		printf("Case #%d: %d\n",i+1,r);
	}


	return 0;
}




