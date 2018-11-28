#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	freopen("ip2.txt","r",stdin);
	freopen("op2.txt","w",stdout);
	int t,k=1;
	scanf("%d",&t);
	while(t--){
		double C,F,X,time=0.0,rate=2.0;
		scanf("%lf %lf %lf",&C,&F,&X);
		double t1,t2;
		t1=X/rate;
		t2=C/rate+X/(rate+F);
		while(t1>t2){
			time+=(C/rate);
			rate=rate+F;
			t1=X/rate;
			t2=C/rate+X/(rate+F);
		}
		time+=t1;
		printf("Case #%d: %.7lf\n",k,time);
		k++;
	}
	return 0;
}	
