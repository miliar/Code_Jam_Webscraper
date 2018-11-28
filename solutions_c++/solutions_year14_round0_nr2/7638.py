#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int re,i;
	double c,f,x,time1,time2,t;
	FILE *fp;
	fp = fopen("out","w");
	scanf("%d",&re);
	for(i=1;i<=re;i++){
		
		t=0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		time1=x/(2.0+t*f);
		while(1){
			t++;
			time2=time1+c/(2.0+(t-1.0)*f)-x/(2.0+(t-1.0)*f)+x/(2.0+t*f);
			if(time2>=time1)
				break;
			else time1=time2;
		}
		fprintf(fp,"Case #%d: %.7lf\n",i,time1);		
	}
	fclose(fp);
} 
