#include <stdio.h>
int min(int a,int b)
{
	if(a<b)
		return a ;
	else 
		return b ;
}
int max(int a,int b)
{
	if(a>b)
		return a;
	else
		return b;
}
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
    int q=1;
	while(t--)
	{
		int x,r,c;
		scanf("%d %d %d",&x,&r,&c);
		int minimum  = min(r,c);
		int maximum = max(r,c);
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",q++);
		}
		else if(x==2)
		{
			if(minimum==1 && (maximum==1 || maximum==3))
				printf("Case #%d: RICHARD\n",q++);
			else if(minimum==3 && maximum==3)
				printf("Case #%d: RICHARD\n",q++);
			else
				printf("Case #%d: GABRIEL\n",q++);
		}
		else if(x==3)
		{
			if((minimum==2 || minimum ==3) && maximum ==3)
				printf("Case #%d: GABRIEL\n",q++);
			else if(minimum==3 && maximum==4)
				printf("Case #%d: GABRIEL\n",q++);
			else
				printf("Case #%d: RICHARD\n",q++);
		}
		else if(x==4)
		{
			if((minimum==4 || minimum==3) && maximum==4)
				printf("Case #%d: GABRIEL\n",q++);
			else
				printf("Case #%d: RICHARD\n",q++);
		}
	}
}
