#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using std::vector;
using std::pair;
using std::make_pair;
using std::sort;
double sr[105],sc[105];
double max(double a,double b){
	return a>b?a:b;
}
int main(void){
	int t,hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		int n;
		scanf("%d",&n);
		double v,x;
		scanf("%lf%lf",&v,&x);
		int i;
		for(i=0;i<n;i++)
		  scanf("%lf%lf",&sr[i],&sc[i]);
		if(n==1){
			if(sc[0]!=x) printf("Case #%d: IMPOSSIBLE\n",hh);
			else printf("Case #%d: %.10lf\n",hh,v/sr[0]);
		}
		else{
			if(sc[0]==sc[1]){
				if(sc[0]!=x) printf("Case #%d: IMPOSSIBLE\n",hh);
				else printf("Case #%d: %.10lf\n",hh,v/(sr[0]+sr[1]));
			}
			else{
				double a=v*(x-sc[1])/(sc[0]-sc[1]),b=v*(x-sc[0])/(sc[1]-sc[0]);
				if(a<0||b<0) printf("Case #%d: IMPOSSIBLE\n",hh);
				else printf("Case #%d: %.10lf\n",hh,max(a/sr[0],b/sr[1]));
			}
		}
	}
	return 0;
}

