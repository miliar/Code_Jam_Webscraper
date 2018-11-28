/*
 * sheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: arup
 */
#include<stdio.h>

int main()
{
	int test_case,i,n,j,res,k,count,val;
	bool used[11];
	freopen("sheep.txt", "rt", stdin);
	freopen("sheep_out.txt", "wt", stdout);
	scanf("%d",&test_case);
	for(i = 1; i <= test_case; i++)
	{
		scanf("%d", &n);
		for(k = 0; k <= 10; k++)
			used[k] = false;
		printf("Case #%d: ",i);
		if(n == 0)
			printf("INSOMNIA\n");
		else
		{
			j = 1;
			count = 0;
			while(count!=10)
			{
				val = n*j;
				res = val;
				while(val)
				{
					int p = val%10;
					if(!used[p])
					{
						used[p] = true;
						count++;
					}
					val = val/10;
				}
				j++;
			}
			printf("%d\n",res);
		}
	}
	return 0;
}



