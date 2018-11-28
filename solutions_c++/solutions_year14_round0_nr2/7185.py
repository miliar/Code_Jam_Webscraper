#include <stdio.h>

int main(){
	FILE *in=fopen("B-large.in","r");
	FILE *out=fopen("output.out","w");
	int t, tt;
	fscanf(in,"%d",&t);
	tt=t;
	while(t--){
		double c,f,x,y=0;
		fscanf(in,"%lf %lf %lf",&c,&f,&x);
		double n=(x*f-2*c)/(c*f);
		if(n<0)
			fprintf(out,"Case #%d: %.7lf\n",tt-t,x/2);
		else {
			for(int i=0;i<(int)n;i++)
				y+=c/(2+f*i);
			y+=x/(2+f*(int)n);
			fprintf(out,"Case #%d: %.7lf\n",tt-t,y);
		}
	}
	fclose(in);
	fclose(out);

	return 0;
}