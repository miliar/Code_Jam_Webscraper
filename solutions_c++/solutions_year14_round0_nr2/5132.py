#include<stdio.h>
int t,i,count;
double c,f,x,summain,sumrest;
int main()
{
	count=0;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		summain=sumrest=0;
		for(i=0;;++i)
		{
			sumrest = summain + x/(2+i*f);
			summain += c/(2+i*f);
			if(summain + x/(2+(i+1)*f) > sumrest)
				break;
		}
		++count;
		printf("Case #%d: %.7lf\n",count,sumrest);
	}
	return 0;
}
