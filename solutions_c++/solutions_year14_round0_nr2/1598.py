#include<stdio.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	double c,f,x,q,ans=0.0,i;
	int t,t2;
	scanf("%d",&t);
	for(t2=1;t2<=t;t2++){
		scanf("%lf %lf %lf",&c,&f,&x);
		q = (x*f-2.0*c)/c/f;
		for(i=0.0;i<q-1.0;i+=1.0){
			ans += c / (2.0+i * f);
		}
		ans += x / (2.0+i*f);
		printf("Case #%d: %.7lf\n",t2,ans);
		ans = 0.0;
	}
	return 0;
}