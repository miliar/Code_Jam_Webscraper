
#include<cstdio>
#include<cstring>
#include<cmath>
const double epx=1e-10;
FILE *fp_in,*fp_out;
int main(){
	int t,k=1;
	if((fp_in=fopen("B-large.IN","r"))==NULL)
	{
		printf("1error\n");
		return 0;
	}
	if((fp_out=fopen("out","w"))==NULL)
	{
		printf("2error\n");
		return 0;
	}
	fscanf(fp_in,"%d",&t);
	while(t--){
		double n=2,c,f,x,time=0;
		fscanf(fp_in,"%lf%lf%lf",&c,&f,&x);
		if(c>x||abs(c-x)<epx)
			time=x/n;
		else {
			time=c/n;
			while(1){
				if(x/(n+f)<(x-c)/n){
					n+=f;
					time+=c/n;
				}
				else break; 
			}
			time+=(x-c)/n;
		}
		fprintf(fp_out,"Case #%d: %.7lf\n",k++,time);
	}
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
