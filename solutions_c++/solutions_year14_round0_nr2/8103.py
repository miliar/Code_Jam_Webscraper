#include<stdio.h>
int main()
{
	FILE *f1,*f2;
	f1=fopen("input.in","r");
	f2=fopen("output.txt","w");
	int t,z;
	double c,f,x,i,j,rate;
	double l,m,n,temp;
	double result;
	fscanf(f1,"%d",&t);
	z=t;
	while(t--)
	{
		rate=2;
		result=0;
		fscanf(f1,"%lf %lf %lf",&c,&f,&x);
		if(c>x)
			result=x/rate;
		else
		{
			x=x-c;
			while((x+c)/(rate+f)<x/rate)
			{
				result=result+(c/(rate));
				rate=rate+f;
				//printf("%lf %lf %lf\n",result,rate,x);
				if(x<0)
				{
					break;
				}	
			}
			x=x+c;
			result=result+x/rate;
			//printf("| %lf %lf\n",result,rate);
		}
		fprintf(f2,"Case #%d: %lf\n",z-t,result);
	}
	return 0;
}
