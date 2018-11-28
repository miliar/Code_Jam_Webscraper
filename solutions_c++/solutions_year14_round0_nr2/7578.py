#include<stdio.h>
FILE *in,*out;
int main()
{
	in=fopen("b.in","r");
	out=fopen("b.out","w");
	int tc,test;
	double c,f,x;
	double v,t;
	fscanf(in,"%d",&tc);
	for(test=1;test<=tc;test++)
	{
		fscanf(in,"%lf%lf%lf",&c,&f,&x);
		t=0.;
		v=2.;
		while( c/f*v+c<x )
		{
			t+=c/v;
			v+=f;
		}
		fprintf(out,"Case #%d: ",test);
		fprintf(out,"%.7f",t+x/v);
		fprintf(out,"\n");
	}
	return 0;
}