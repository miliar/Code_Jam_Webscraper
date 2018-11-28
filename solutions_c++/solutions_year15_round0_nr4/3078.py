#include <stdio.h>
#include <stdlib.h>
#include <queue>

using namespace std;

int main()
{
	int t,x,r,c,i,max_l,max_b,max,min;
	scanf("%d",&t);

	for(i=1;i<=t;i++)
	{
		scanf("%d",&x);
		scanf("%d",&r);
		scanf("%d",&c);

		if(r>=c)
		{
			max = r;
			min = c;
		}
		else
		{
			max = c;
			min = r;
		}

		if(x%2 ==0)
		{
			max_l = (x/2) + 1;
			max_b = x/2;
		}
		else
		{
			max_l = (x/2) + 1;
			max_b = max_l;
		}

		if(min <= 0)
		{
			printf("Case #%d: RICHARD\n",i);
		}
		else if(max < x)
		{
			printf("Case #%d: RICHARD\n",i);
		}
		else if(min >= max_b) // Gabriel may win
		{
			if(x == 4 && min ==2)
			{
				printf("Case #%d: RICHARD\n",i);
			}
			else
			{
				int value = (r*c) - x;
				if(value%x ==0) // Gabriel
				{
					printf("Case #%d: GABRIEL\n",i);
				}
				else
				{
					printf("Case #%d: RICHARD\n",i);
				}
			}
		}
		else
		{
			printf("Case #%d: RICHARD\n",i);
		}

	}
	return 0;
}
