#include <stdio.h>
#include <algorithm>
using namespace std;

main(){
	int tests;
	scanf("%d",&tests);
	for(int casenum=1;casenum<=tests;casenum++){
		printf("Case #%d: ",casenum);
		double v0=2,v1;
		double c,x;
		scanf("%lf%lf%lf",&c,&v1,&x);
		double ans=1e9;
		double t=0;
		for(int k=0;k<1000000;k++){
			ans=min(ans,t+x/(v0+k*v1));
			t+=c/(v0+k*v1);
		}
		printf("%.7f\n",ans);
	}
}