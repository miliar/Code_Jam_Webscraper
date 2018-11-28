#include <stdio.h>
int main(){
	int t,n,i;
	double c,f,x,d;
	FILE *f1,*f2;
	f1=fopen("B-large.in","r");
	f2=fopen("su.txt","w");
	fscanf(f1,"%d\n",&t);
	for(n=0;n<t;n++){
		d=0;
		fscanf(f1, "%lf %lf %lf\n",&c,&f,&x);
		for(i=0;;i++){
			if((2+f*(i+1))*(x-c)>(2+f*i)*x){
				d+=c/(2+f*i);
			}
			else{
				d+=x/(2+f*i);
				break;
			}
		}
		fprintf(f2,"Case #%d: %.7lf\n",n+1,d);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}