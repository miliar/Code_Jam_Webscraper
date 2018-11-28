#include<conio.h>
#include<stdio.h>
void main()
{
	freopen("input.in","r",stdin);
	freopen("murali.txt","w",stdout);
	int t,r[64],c[64],x[64],flag=0;
	scanf("%d\n",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d %d %d",&x[i],&r[i],&c[i]);
	}
	for(i=0;i<t;i++)
	{
		if(x[i]==1)
			flag=1;
		else if(x[i]==2)
		{
			if(r[i]*c[i]%2==0)
				flag=1;
			else
				flag=0;
		}
		else if(x[i]==3)
		{
			if((r[i]*c[i]!=3)&&((r[i]*c[i])%3==0))
				flag=1;
			else
				flag=0;
		}
		else if(x[i]==4)
		{
			if(((r[i]*c[i])==12)||((r[i]*c[i])==16))
				flag=1;
			else
				flag=0;
		}
		if(flag==0)
		{
			printf("Case #%d: ",i+1);
			printf("RICHARD\n");
		}
		else
		{
			printf("Case #%d: ",i+1);
			printf("GABRIEL\n");
		}
	}

}




