#include<stdio.h>
int main()
{
	int t,count;char c,d;
	scanf("%d",&t);
	scanf("%c",&c);
	for(int i=0;i<t;i++)
	{
		count=1;c=0;d=0;
		scanf("%c",&c);
		while(1)
		{
			scanf("%c",&d);
			if(d=='\n')
			{
				if(c=='+')
				count--;
				break;
			}
			if(c!=d)
			count++;
			c=d;
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
