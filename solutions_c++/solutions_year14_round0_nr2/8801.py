#include <stdio.h>
using namespace std;
FILE *in,*out;
int main()
{
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	int t;
	int z;
	double c,f,x,y,a,b;
	fscanf(in,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		fscanf(in,"%lf%lf%lf",&c,&f,&x);
		z=(int)(1e-14+x/c-2/f);
		if (z<0) z=0;
		y=x/(2.0+f*z);
		for (int j=0;j<z;j++) y+=c/(2.0+f*j);
		fprintf(out,"Case #%d: %.7lf\n",i,y);
	}
	fclose(in);
	fclose(out);
	return 0;
}
