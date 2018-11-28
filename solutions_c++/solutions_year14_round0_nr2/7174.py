#include<stdio.h>
#include<stdlib.h>

double etime = 0.0000000;

double click(double c,double f,double x,double r)
{
	if( (x/r) < (c/r)+(x/(r+f)))
	return (x/r);
	else{
	etime = etime + (c/r);
	r=r+f;
	return(click(c,f,x,r));
	}
}


int main()
{
	int t,i;
	double c,f,x,r,las,ans;
	r=2.0000000;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%lf %lf %lf",&c,&f,&x);
		las = click(c,f,x,r);
		ans = las + etime;
		printf("Case #%d: %f\n",i,ans);
		etime=0.0000000;
	}
return 0;
}
