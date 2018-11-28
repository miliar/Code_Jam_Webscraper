#include <stdio.h>
int main()
{
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		int a[10]={0};
		int n,j,k,p=1,d,x,c=0,flag=0;
		scanf("%d",&n);
		if(n == 0)
		printf("Case #%d: INSOMNIA\n",i);
		else
		{
		for(j=1;j<=1000;j++)
		{
			p=j*n;
			x=p;
			while(p!=0)
			{
				d=p%10;
				(a[d])++;
				p/=10;
			}
			if(a[0]>=1&&a[1]>=1&&a[2]>=1&&a[3]>=1&&a[4]>=1&&a[5]>=1&&a[6]>=1&&a[7]>=1&&a[8]>=1&&a[9]>=1)
				flag=1;
			if(flag==1)
			{
				printf("Case #%d: %d\n",i,x);
				break;
			}
		}
	}
	}
	return 0;
}

