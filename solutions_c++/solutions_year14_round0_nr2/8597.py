#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	double c,f,x,ans,temp,atemp,ctemp;
	for(int i=1;i<=t;i++){
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=1000000.0;
		temp=0.0,ctemp=2;
		atemp=0.0;
		while(1){
			atemp=temp+x/ctemp;
			temp+=c/ctemp;
			ctemp+=f;
			if(atemp<ans) ans=atemp;
			if(atemp>ans) break;
		}
		printf("Case #%d: %.7lf\n",i,ans);
	}
	return 0;
}