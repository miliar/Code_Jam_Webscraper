#include <stdio.h>
#include <math.h>

const double eps=1e-8;

int main()
{
	freopen("D:\\1.in","r",stdin);
	freopen("D:\\out.out","w",stdout);
	double pi=acos(-1.0);
	int T,r,x,ii,i,t,sum;
	scanf("%d",&T);
	ii=1;
	while (T--)
	{
		scanf("%d%d",&r,&t);
		x=r+1;i=0;
		sum=(x*x-r*r);
		while(t>=sum)
		{	
			t-=sum;
			r=x+1;
			x=r+1;
			i++;
			sum=(x*x-r*r);
		}
		printf("Case #%d: %d\n",ii++,i);
	}
	return 0;
} 
