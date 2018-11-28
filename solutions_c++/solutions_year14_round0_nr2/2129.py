#include<stdio.h>
int main(){
	int t,z;
	double c,f,x,a,ans,tmp,n;
	scanf("%d",&t);
	for(z=1;z<=t;z++){
		scanf("%lf %lf %lf",&c,&f,&x);
		ans=x/2;
		a=0;
		n=2;
		while(1){
			tmp=ans;
			a+=c/n;
			n+=f;
			ans=a+(x/n);
			if(ans>=tmp)
				break;
		}
		printf("Case #%d: %.7lf\n",z,tmp);
	}
	return 0;
}
