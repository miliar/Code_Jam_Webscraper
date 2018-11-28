#include<stdio.h>

int TT,T;
double c,f,x,r,b,ans;

int main(){
	int i;
	scanf("%d",&TT);
	while(TT--){
		scanf("%lf%lf%lf",&c,&f,&x);
		r=2;b=0;
		ans=x/r;
		for(i=1;;i++){
			b+=c/r;
			r+=f;
			if(ans>b+x/r)
				ans=b+x/r;
			else break;
		}
		printf("Case #%d: %.7lf\n",++T,ans);
	}
	return 0;
}