#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
double c,f,x;
int T;
const double eps=1e-8;
int main(){
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=x/2;
		double tmp=0;
		double tmpc=2;
		int i=0;
		while(1){
			tmp=tmp+c/tmpc;
			tmpc=tmpc+f;
			double tmpt=tmp+x/tmpc;
			if(tmpt+eps>=ans) break;
			ans=min(ans,tmpt);
			i++;
		}
		printf("Case #%d: %.7lf\n",ca++,ans);
	}
	return 0;
}
