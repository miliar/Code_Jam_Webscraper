#include<stdio.h>

int main(void)
{
	freopen("C:\\Users\\user\\Desktop\\i.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\out1.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int ans=0,x,r,c;
		scanf("%d%d%d",&x,&r,&c);
		if(x==1)
		ans=1;
		else if(x==2)
		{
			if(r%2==0||c%2==0)
			ans=1;
		}
		else if(x==3)
		{
			if(r*c>=6&&(r*c)%3==0)
			ans=1;
		}
		else
		{
			if(r*c>=12)
			ans=1;
		}
		if(ans==1)
		printf("Case #%d: GABRIEL\n",i);
		else
		printf("Case #%d: RICHARD\n",i);
	}
	return 0;
}
