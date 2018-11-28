#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		if(x==1)
			printf("Case #%d: GABRIEL\n",i+1);
		else if(x==2)
		{
			if(r%2==0 || c%2==0)
				printf("Case #%d: GABRIEL\n",i+1);
			else
				printf("Case #%d: RICHARD\n",i+1);
		}
		else if(x==3)
		{
			if((r<=2 && c<=2) || ((r==3 && c==1) || (r==1 && c==3)) || (r==4 && c<=2) || (r<=2 && c==4) || (r==4 && c==4))
				printf("Case #%d: RICHARD\n",i+1);
			else
				printf("Case #%d: GABRIEL\n",i+1);
			
		}
		else
		{
			if(r<=3 && c<=3 || (r==4 && c<=2) || (r<=2 && c==4) )
				printf("Case #%d: RICHARD\n",i+1);
			else
				printf("Case #%d: GABRIEL\n", i+1);
		}
	}
}
