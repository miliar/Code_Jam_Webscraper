#include <stdio.h>

int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0; e<t ; e++ ){
		long double goal,cost,extra;
		scanf("%Lf %Lf %Lf",&cost,&extra,&goal);
		printf("Case #%d: ",e+1);
		long double cal = 2;
		long double ans = 100000;
		long double tbuy = 0;
		long double tot ;
		for(int i = 0 ; i <= goal ; i++ ){
			tot = tbuy+goal/cal;
			if( tot < ans ) ans = tot;
			tbuy += cost/cal;
			cal += extra;
		}
		printf("%.7Lf\n",ans);
	}
}
