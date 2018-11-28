#include <stdio.h>
#include <string.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,i;
	double c,f,x;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		scanf("%lf %lf %lf",&c,&f,&x);
		double t=0.0;
		double tmp=2.0;
		double money=0.0;
		if(x<=c){
			t=x/tmp;
		} else {
			while(1){
				double _t=(x/tmp);
				double r_t=(c/tmp + x/(tmp+f) );
				if(_t<=r_t){
					t+=_t;
					break;
				}
				t+=(c/tmp);
				tmp+=f;
			}
		}
		printf("Case #%d: %.7lf\n",i,t);
	}
	return 0;
}