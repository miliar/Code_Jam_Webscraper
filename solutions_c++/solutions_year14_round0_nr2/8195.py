//Vandit Jain, MNNIT Allahabad
#include<stdio.h>
main(){
	int t;
	double c,f,x;
	scanf("%d",&t);
	int ca=0;
	while(t--){
		ca++;
		scanf("%lf %lf %lf",&c,&f,&x);
		double to,tn,p=2.0,tm;
		if(x<=c){
			printf("Case #%d: %lf\n",ca,x/(2.0));
			continue;
		}
		to=x/p;
		tm=c/p;
		tn=tm+x/(p+f);
		while(tn<to){
			to=tn;
			p+=f;
			tm+=(c/p);
			tn=tm+x/(p+f);
		}
		printf("Case #%d: %lf\n",ca,to);
	}
	return 0;
}