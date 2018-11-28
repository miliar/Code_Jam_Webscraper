#include<stdio.h>
int a[10];
int check(int n)
{
	int z;
	while(n!=0)
	{
		z=n%10;
		a[z]=1;
		n=n/10;
	}
}
int check1()
{
	int i,k=0;
	for(i=0;i<10;i++)
	{
		if (a[i]==1)
			{
			
				k++;
			}
	}
	if(k==10)
		return 1;
	else
		return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,z;
	scanf("%d",&t);
	int i;
	int m=1;
	while(t--)
	{
		int r=1;
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		scanf("%d",&z);
		if(z==0)
		{
			printf("Case #%d: INSOMNIA\n",m);
		}
		else
		{
		
			while(check1()==0)
			{
				check(z*r);
				r+=1;				
			}
			printf("Case #%d: %d\n",m,z*(r-1));
		}
		m++;
	}
}
