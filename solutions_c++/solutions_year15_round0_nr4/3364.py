#include <stdio.h>
#include <string.h>

//int A[1000];

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
	int X,R,C;

	scanf("%d",&N);

	for (i=0;i<N;i++)
	{
		scanf("%d%d%d",&X,&R,&C);
		int temp = R*C;

		if (X == 1)
			printf("Case #%d: GABRIEL\n",i+1);
		else if (X==2)
		{
			if ((temp % X)==0)	
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);
		}
		else if (X>=3)
		{
			if (C<=X-1 && R<=X-1)
				printf("Case #%d: RICHARD\n",i+1);
			else if (C<=X-2 || R<=X-2)
				printf("Case #%d: RICHARD\n",i+1);
			else if ((temp % X)==0 && temp>=X)
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);

		}


	}
	
	return 0;
}




