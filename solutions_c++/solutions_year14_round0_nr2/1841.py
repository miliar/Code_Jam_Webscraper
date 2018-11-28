#include <stdio.h>

int main()
{
	int tcase;
	double c,f,x,pow;
	double re,temp,sum;

	FILE *in,*out;
	in=fopen("B-large.in","r");
	out=fopen("output2.txt","w");

	fscanf(in,"%d",&tcase);
	for(int t=0;t<tcase;t++)
	{
		fscanf(in,"%lf%lf%lf",&c,&f,&x);
		pow=2.0;
		re=x/pow;
		sum=0;
		while(1)
		{
			sum+=c/pow;
			temp=sum+(x/(pow+f));
			if(re>temp)
			{
				re=temp;
				pow+=f;
			}
			else
				break;
		}
		fprintf(out,"Case #%d: %.7lf\n",t+1,re);
	}
	return 0;
}