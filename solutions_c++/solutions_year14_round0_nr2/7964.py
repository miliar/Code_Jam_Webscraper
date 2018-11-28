#include<stdio.h>
int main()
{
	 int t,d=1;
	double c,f,x,sum,k,t1,t2,g;
	scanf("%ld",&t);
	for(;t--;)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		sum=0;
		k=2;
		for(;;)
		{
			t1=x/k;
			g=k+f;
			t2=(c/k)+(x/g);
			if(t2<t1)
			{
			sum+=c/k;	
			k=k+f;
			
		}
		else
		{
			sum+=t1;
			break;
		}
		}
		printf("case #%d: %.7f\n",d++,sum);
	}

}
