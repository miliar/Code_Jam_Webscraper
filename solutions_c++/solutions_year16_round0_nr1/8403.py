#include<stdio.h>
int array[10];
int digitcounter(int z)
{
	while(z!=0)
	{
		array[z%10]=1;
		z=z/10;
	}
}
int arraycheck()
{
	int i,z=0;;
	for(i=0;i<10;i++)
	{
		if(array[i]==1)
		{
			z++;
		}
	}
	if(z==10)
		return 1;
	else
		return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int test,j,number,m=1;
	scanf("%d",&test);
	while(test--)
	{
		int h=1;
		scanf("%d",&number);
		for(j=0;j<10;j++)
		{
			array[j]=0;
		}
		if(number==0)
		{
			printf("Case #%d: INSOMNIA\n",m);
		}
		else
		{
			while(arraycheck()==0)
			{
				digitcounter(number*h);	
				h++;
			}
			printf("Case #%d: %d\n",m,number*(h-1));
		}
		m++;
	}
}
