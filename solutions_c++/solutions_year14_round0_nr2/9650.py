#include <stdio.h>
int t;
int shop = 1;
double c,f,x;
double time1,time2;
double co;
int main(void)
{
	int i,j,k;

	FILE *in = fopen("B-small-attempt0.in","r");
	FILE *out = fopen("output.txt","w");
	
	fscanf(in,"%d",&t);
	while(t--)
	{
		co=2;
		time1=0;
		time2=99999999999;

		fscanf(in,"%lf %lf %lf",&c,&f,&x);
		for(i=0; ; i++)
		{
			time1=0;
			for ( j=0; j<i; j++)
			{
				time1+=(c/(co+(f*(j))));	
				
			}

			time1+=(x/(co+(f*(i))));
			if(time1 > time2)
			{
				break;
			}
			else
			{
				time2= time1;
			}
		}
		fprintf(out,"Case #%d: %.7lf\n",shop++,time2);
	}
	return 0;
}