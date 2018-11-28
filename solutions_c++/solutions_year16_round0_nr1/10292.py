#include <stdio.h>

int fre[11];

void clear ()
{
	for(int i=0;i<=10;i++)
		fre[i]=0;
}

bool check ()
{
	int count = 0;
	for(int i=0;i<=10;i++)
		if(fre[i]!=0)
			count++;
	if(count == 10)
		return true;
	else
		return false;
}

void mod (int num)
{
	while (num!=0)
	{
		fre[num%10]++;
		num/=10;
	}
}

int main()
{
	int t,n;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",i);
		else
		{
			int nn=1;
			int mul=1;
			while (!check())
			{
				nn=n*mul;
				mod(nn);
				mul++;
			}
			clear();
			printf("Case #%d: %d\n",i,nn);
		}
	}
}