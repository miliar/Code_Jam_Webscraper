#include<stdio.h>

int main()
{
	int T,X,R,C;
	freopen ("D:\\Input.txt","rb",stdin);
	freopen ("D:\\Output1.txt","wb",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d %d %d",&X,&R,&C);
		if(X==1)
		{
			printf("Case #%d: GABRIEL\n",i);
			continue;
		}
		if(X==2)
		{
			if((R*C)%2)
			{
				printf("Case #%d: RICHARD\n",i);
				continue;
			}
			else
			{
				printf("Case #%d: GABRIEL\n",i);
				continue;
			}
		}
		if(X==3)
		{
			int RC = R*C;
			if(RC==6 || RC ==9 || RC == 12)
			{
				printf("Case #%d: GABRIEL\n",i);
				continue;
			}
			else
			{
				printf("Case #%d: RICHARD\n",i);
				continue;
			}
		}
		if(X==4)
		{
			int RC = R*C;
			if(RC>=12)
			{
				printf("Case #%d: GABRIEL\n",i);
				continue;
			}
			else
			{
				printf("Case #%d: RICHARD\n",i);
				continue;
			}
		}
	}
	return 0;
}