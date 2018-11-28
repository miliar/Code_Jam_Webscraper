#include<stdio.h>
#include<stdlib.h>
#define err 10000
int main(void){
	freopen("2014Q_pB_L.in","r",stdin);
	freopen("2014Q_pB_L.txt","w",stdout);
	int t,hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		int i;
		int p=(int)(f*x-2*c-f*c)/(f*c);
		x=x*err;
		c=c*err;
		double ans=10000000*err;
		double ttt=0;
		if(ans>x/2) ans=x/2;
		for(i=0;i<=p+2;i++){
			ttt+=c/(2+i*f);
			if(ttt+x/(2+(i+1)*f)<ans) ans=ttt+x/(2+(i+1)*f);
		}
		printf("Case #%d: %.7lf\n",hh,ans/err);
	}
	return 0;
} 
