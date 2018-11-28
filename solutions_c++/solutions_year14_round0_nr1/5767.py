#include <stdio.h>

int result[16+1];

int main()
{
	int i,j,k,w,T,x;
	freopen("A.in","r",stdin);
	scanf("%d",&T);
	for (w=1; w<=T; ++w)
	{
		printf("Case #%d: ",w);
		for (i=1; i<=16; ++i)
			result[i]=0;
		scanf("%d",&k);
		for (i=1; i<=4; ++i)
		{
			for (j=1; j<=4; ++j)
				{
					scanf("%d",&x);
					if (i==k)
						++result[x];
				}
		}

		scanf("%d",&k);
		for (i=1; i<=4; ++i)
		{
			for (j=1; j<=4; ++j)
				{
					scanf("%d",&x);
					if (i==k)
						++result[x];
				}
		}
	
		k=0;
		for (i=1; i<=16; ++i)
			if (result[i]==2)
			{
				++k;
				j=i;
			}
		if (k==1)
			printf("%d\n",j);
		else if (k==0)
			printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
