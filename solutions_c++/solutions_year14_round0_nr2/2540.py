#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	float c,f,x,initial,a,b,d,flag=0,time; int i;
	for(i=0;i<t;i++)
	{
		scanf("%f %f %f",&c,&f,&x);
		initial=2; time=0;
		while(flag!=1)
		{
			a=x/initial;
			b=initial+f;
			d=(c/initial)+(x/b);
			if(d<a)
			time=time+(c/initial);
			else
			{
				time=time+(x/initial);
				break;
			}
			initial=initial+f;
		}
		printf("Case #%d: ",i+1);
		printf("%.07f\n",time);
	}
	return 0;
}
