#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int t;

	scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		int x,r,c;

		scanf("%d%d%d",&x,&r,&c);

		printf("Case #%d: ",i+1);

		if(x==1)
			printf("GABRIEL\n");
		else if(x==2)
		{
			if(r%2==0 || c%2==0)
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
		}

		else if(x==3)
		{
			if(!(r==2 && c==2))
			{
			if(((r==3 || r==2) && (c==2 || c==3)) || (r==3 && c==4) || (r==4 && c==3))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
			}
			else
				printf("RICHARD\n");
		}

		else if(x==4)
		{
			if(!(r==3 && c==3))
			{
			if((r==3 || r==4) && (c==3 || c==4))
				printf("GABRIEL\n");
			else
				printf("RICHARD\n");
			}
			else
				printf("RICHARD\n");
		}
	}

	return 0;

}

