#include <stdio.h>

int main()
{
	int tc, ct;
	scanf("%d",&tc);
	for(int ct=1;ct<=tc;ct++)
	{
		printf("Case #%d: ", ct);
		int a, b, k;
		scanf("%d %d %d", &a, &b, &k);
		int res = 0;
		int i, j;
		for(i=0;i<a;i++)
			for(j=0;j<b;j++)
				if((i & j) < k)
					res++;
		printf("%d\n",res);
	}
	return 0;
}
